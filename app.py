import streamlit as st
import pandas as pd
import os

st.title("Varianten-Auswahl")

csv_file = "variables_template.csv"

if not os.path.exists(csv_file):
    st.error(f"{csv_file} nicht gefunden!")
    st.stop()

try:
    df = pd.read_csv(csv_file)
    st.success("CSV erfolgreich geladen!")
except Exception as e:
    st.error(f"Fehler beim Lesen: {e}")
    st.stop()

# Varianten-Auswahl
variants = sorted(df["Variant"].dropna().unique().tolist())
sel_variants = st.multiselect("Varianten auswählen", variants, default=variants[:1])

# Gefilterte Tabelle
filtered = df[df["Variant"].isin(sel_variants)].copy()
st.write("### Ausgewählte Positionen")
st.dataframe(filtered, use_container_width=True)
