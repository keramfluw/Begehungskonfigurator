import streamlit as st
import os

st.title("Filesystem-Debug")

# Alle Dateien im aktuellen Verzeichnis anzeigen
files = os.listdir(".")
st.write("### Dateien im aktuellen Verzeichnis:")
for f in files:
    st.text(f)

# Prüfen, ob CSV vorhanden ist
csv_file = "variables_template.csv"
if csv_file in files:
    st.success(f"{csv_file} gefunden!")
    try:
        with open(csv_file, "r", encoding="utf-8") as fh:
            content = fh.read(500)  # nur die ersten 500 Zeichen
        st.write("### Erster Inhalt der CSV:")
        st.text(content)
    except Exception as e:
        st.error(f"Fehler beim Lesen der CSV: {e}")
else:
    st.error(f"{csv_file} nicht gefunden!")
