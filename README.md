# Varianten-Auswahl App

Diese Version lädt die Datei `variables_template.csv`, bietet eine Multiselect-Auswahl der Spalte `Variant` und zeigt nur die ausgewählten Positionen an.

## Dateien
- `app.py` – Streamlit-App
- `requirements.txt` – Python-Abhängigkeiten
- `variables_template.csv` – Vorlage-Datei mit Daten

## Start
```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```
