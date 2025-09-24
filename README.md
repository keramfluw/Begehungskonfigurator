# Streamlit Diagnostik

Diese App **stürzt nicht ab** und zeigt stattdessen Diagnoseinformationen an:

- Python-/Plattform-Version
- Vorhandene Dateien im Arbeitsverzeichnis
- Voransicht der `variables_template.csv` (roh, mit Encoding-Vermutung)
- Robuster Ladeversuch der CSV mit `pandas` (mehrere Encodings & Separatoren)

## Start
```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```
