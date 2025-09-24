import streamlit as st
import os, sys, platform, traceback

st.set_page_config(page_title="Streamlit Diagnostik", layout="wide")
st.title("🩺 Streamlit Diagnostik – Umgebung & CSV")
st.caption("Ziel: App startet IMMER, zeigt Diagnose statt Abbruch.")

# --- Environment info
st.markdown("## Umgebung")
cols = st.columns(3)
cols[0].write(f"**Python:** {sys.version.split()[0]}")
cols[1].write(f"**Platform:** {platform.platform()}")
cols[2].write(f"**Arbeitsverzeichnis:** `{os.getcwd()}`")

# Packages
st.markdown("### Paket-Versionen")
def safe_import(name):
    try:
        mod = __import__(name)
        ver = getattr(mod, "__version__", "unbekannt")
        st.success(f"{name}: {ver}")
        return mod, ver, None
    except Exception as e:
        st.error(f"{name}: Import-Fehler → {e}")
        return None, None, e

streamlit_mod, _, _ = safe_import("streamlit")
pandas_mod, pandas_ver, pandas_err = safe_import("pandas")

# --- Filesystem
st.markdown("## Dateien im Verzeichnis")
files = sorted(os.listdir("."))
st.code("\n".join(files) or "(leer)")

# --- CSV presence & preview
CSV_NAME = "variables_template.csv"
st.markdown(f"## CSV-Prüfung: `{CSV_NAME}`")
if CSV_NAME in files:
    st.success(f"Datei gefunden: {CSV_NAME}")
    try:
        with open(CSV_NAME, "rb") as fh:
            raw = fh.read(8000)  # max 8KB Preview
        try:
            preview = raw.decode("utf-8")
            enc = "utf-8"
        except UnicodeDecodeError:
            try:
                preview = raw.decode("utf-8-sig")
                enc = "utf-8-sig"
            except UnicodeDecodeError:
                try:
                    preview = raw.decode("latin-1")
                    enc = "latin-1"
                except Exception as e:
                    preview = f"(Decoding fehlgeschlagen: {e})"
                    enc = "unbekannt"
        st.write(f"**Encoding-Vermutung:** {enc}")
        st.text(preview[:500])
    except Exception as e:
        st.error(f"Fehler beim Lesen der CSV (raw): {e}")
else:
    st.warning(f"{CSV_NAME} nicht gefunden.")

# --- Robust CSV load (mit/ohne Pandas)
st.markdown("## CSV laden (robust)")
def try_load_csv(file):
    results = []
    encodings = ["utf-8", "utf-8-sig", "latin-1"]
    seps = [",", ";", "\t", "|"]
    if pandas_mod is None:
        st.info("Pandas nicht verfügbar – nur Rohvorschau möglich.")
        return results
    import pandas as pd
    for enc in encodings:
        for sep in seps:
            try:
                df = pd.read_csv(file, encoding=enc, sep=sep, engine="python")
                results.append((enc, sep, df))
            except Exception as e:
                results.append((enc, sep, e))
    return results

if CSV_NAME in files:
    tries = try_load_csv(CSV_NAME)
    ok = [(enc, sep, df) for (enc, sep, df) in tries if not isinstance(df, Exception)]
    if pandas_mod and ok:
        enc, sep, df = ok[0]
        st.success(f"Erfolgreich mit Pandas gelesen → Encoding='{enc}', Separator='{sep}', Zeilen={len(df)}")
        st.write("### Spaltennamen:", list(df.columns))
        st.dataframe(df.head(10), use_container_width=True)
    elif pandas_mod and not ok:
        st.error("Pandas konnte die CSV nicht lesen. Letzte Fehler:")
        for enc, sep, err in tries[-4:]:
            if isinstance(err, Exception):
                st.code(f"{enc} | {sep} → {type(err).__name__}: {err}")
else:
    st.info("Keine CSV-Ladeversuche, da Datei fehlt.")

st.markdown("---")
st.markdown("Falls weiterhin Probleme auftreten, exportiere bitte einen Screenshot dieser Seite oder kopiere die Abschnitte **Paket-Versionen** und **CSV-Prüfung**.")
