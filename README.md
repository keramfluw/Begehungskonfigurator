# CSV-Test App

Diese Version lädt die Datei `variables_template.csv` und zeigt den Inhalt in einer Tabelle an.

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
