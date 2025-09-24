import streamlit as st
import pandas as pd

st.set_page_config(page_title="Wirtschaftlichkeits-Konfigurator (Minimal)", layout="wide")

st.title("⚙️ Minimal-Version Wirtschaftlichkeits-Konfigurator")

@st.cache_data
def load_variables(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    return df

# CSV laden
try:
    df = load_variables("variables_template.csv")
except Exception as e:
    st.error(f"Konnte CSV nicht laden: {e}")
    st.stop()

# Varianten-Auswahl
variants = sorted(df["Variant"].dropna().unique().tolist())
sel_variants = st.multiselect("Varianten auswählen", variants, default=variants[:1])

# Gefilterte Tabelle
work_df = df[df["Variant"].isin(sel_variants)].copy()
st.write("### Ausgewählte Positionen")
st.dataframe(work_df, use_container_width=True)

# Einfache Gesamtkosten
if "Baseline_Cost_EUR" in work_df.columns:
    total = work_df["Baseline_Cost_EUR"].sum()
    st.metric("Summe Baseline-Kosten", f"{total:,.2f} €".replace(",", "X").replace(".", ",").replace("X","."))
else:
    st.info("Keine Kostenspalte gefunden.")
