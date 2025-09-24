# Varianten-Auswahl App

Diese Version lädt die Datei `variables_template.csv`, bietet eine Multiselect-Auswahl über die Spalte `Variant` und zeigt nur die ausgewählten Positionen.

## Dateien
- `app.py` – Streamlit-App mit Varianten-Auswahl
- `requirements.txt` – Abhängigkeiten
- `variables_template.csv` – Testdatei

## Start
```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```
