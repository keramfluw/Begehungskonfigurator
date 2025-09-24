import streamlit as st
import pandas as pd

st.title("CSV-Test")

# CSV laden
try:
    df = pd.read_csv("variables_template.csv")
    st.success("CSV erfolgreich geladen!")
    st.dataframe(df, use_container_width=True)
except Exception as e:
    st.error(f"Konnte CSV nicht laden: {e}")
