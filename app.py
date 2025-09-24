import streamlit as st
import pandas as pd
import os

st.title("CSV-Lese-Test")

csv_file = "variables_template.csv"

if not os.path.exists(csv_file):
    st.error(f"{csv_file} nicht gefunden!")
    st.stop()

try:
    df = pd.read_csv(csv_file)
    st.success("CSV erfolgreich mit Pandas geladen!")

    st.write("### Spaltennamen:")
    st.write(list(df.columns))

    st.write("### Erste 5 Zeilen als Tabelle:")
    st.dataframe(df.head(), use_container_width=True)
except Exception as e:
    st.error(f"Fehler beim Lesen mit Pandas: {e}")
