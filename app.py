
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Qrauts – Minimal App", layout="wide")

st.title("Qrauts – Minimal App (Testversion)")
st.caption("Basisfunktion: Katalog laden, Tabelle editieren, Summen berechnen.")

@st.cache_data
def load_catalog():
    import os
    if not os.path.exists("catalog.csv"):
        return pd.DataFrame([
            {"Variante":"V1 - Test","Tätigkeit":"Dummy-Check","Stunden":1.0,"Satz":75.0,"VK":150.0}
        ])
    df = pd.read_csv("catalog.csv")
    # Falls die CSV aus der großen App kommt, nur eine Minimalstruktur ableiten
    if "variant" in df.columns:
        df = df.rename(columns={"variant":"Variante","activity":"Tätigkeit"})
        if "default_hours" in df.columns: df["Stunden"] = df["default_hours"]
        if "default_internal_rate" in df.columns: df["Satz"] = df["default_internal_rate"]
        if "default_sale_price" in df.columns: df["VK"] = df["default_sale_price"]
    return df[["Variante","Tätigkeit","Stunden","Satz","VK"]]

catalog = load_catalog()

st.markdown("### Positionen (editierbar)")
edited = st.data_editor(
    catalog,
    hide_index=True,
    num_rows="dynamic",
    use_container_width=True
)

st.markdown("### Summen")
if not edited.empty:
    edited["Kosten"] = edited["Stunden"] * edited["Satz"]
    edited["Umsatz"] = edited["VK"]
    summe_kosten = edited["Kosten"].sum()
    summe_umsatz = edited["Umsatz"].sum()
    marge = summe_umsatz - summe_kosten
    st.write(f"**Kosten gesamt:** {summe_kosten:.2f} €")
    st.write(f"**Umsatz gesamt:** {summe_umsatz:.2f} €")
    st.write(f"**Deckungsbeitrag:** {marge:.2f} €")
else:
    st.info("Keine Positionen geladen.")
