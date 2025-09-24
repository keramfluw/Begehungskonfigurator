import streamlit as st
import pandas as pd

st.title("CSV-Debug-App")

try:
    df = pd.read_csv("variables_template.csv")
    st.success("CSV erfolgreich geladen!")
    st.write("### Spaltennamen:")
    st.write(list(df.columns))
    st.write("### Erste 5 Zeilen:")
    st.dataframe(df.head(), use_container_width=True)
except Exception as e:
    st.error(f"Fehler beim Laden der CSV: {e}")
