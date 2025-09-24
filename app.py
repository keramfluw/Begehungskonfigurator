import streamlit as st
import pandas as pd
import os

st.title("CSV-Detail-Debug")

file_path = "variables_template.csv"

if not os.path.exists(file_path):
    st.error(f"Datei {file_path} nicht gefunden!")
    st.stop()

try:
    df = pd.read_csv(file_path)
    st.success("CSV geladen!")
    st.write("### Spaltennamen in der CSV:")
    for col in df.columns:
        st.text(f"- '{col}'")
    st.write("### Erste Zeilen (raw):")
    st.dataframe(df.head(), use_container_width=True)
except Exception as e:
    st.error(f"Fehler beim Lesen der CSV: {e}")
