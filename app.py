import streamlit as st
import pandas as pd

st.title("Varianten-Auswahl")

# CSV laden
try:
    df = pd.read_csv("variables_template.csv")
    st.success("CSV erfolgreich geladen!")
except Exception as e:
    st.error(f"Konnte CSV nicht laden: {e}")
    st.stop()

# Varianten ermitteln
if "Variant" not in df.columns:
    st.error("Die CSV enthält keine Spalte 'Variant'.")
    st.stop()

variants = sorted(df["Variant"].dropna().unique().tolist())
sel_variants = st.multiselect("Varianten auswählen", variants, default=variants[:1])

# Tabelle gefiltert anzeigen
filtered = df[df["Variant"].isin(sel_variants)].copy()
st.write("### Ausgewählte Positionen")
st.dataframe(filtered, use_container_width=True)
