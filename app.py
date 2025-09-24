import streamlit as st
import pandas as pd
import os

st.title("Robuste Varianten-Auswahl")

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

if "Variant" not in df.columns:
    st.error("Spalte 'Variant' fehlt in der CSV!")
    st.write("Gefundene Spalten:", list(df.columns))
    st.stop()

# Variantenliste robust erzeugen
variants = sorted([str(v) for v in df["Variant"].unique() if pd.notna(v)])

if not variants:
    st.warning("Keine Varianten in der CSV gefunden.")
    st.stop()

sel_variants = st.multiselect("Varianten auswählen", variants, default=variants[:1])

if not sel_variants:
    st.info("Bitte mindestens eine Variante auswählen.")
else:
    filtered = df[df["Variant"].astype(str).isin(sel_variants)].copy()
    st.write("### Ausgewählte Positionen")
    st.dataframe(filtered, use_container_width=True)
    st.write(f"**{len(filtered)} Zeilen gefiltert.**")
