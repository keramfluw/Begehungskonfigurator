# CSV-Debug App

Diese Version dient nur zur Analyse der CSV-Struktur.  
Sie lädt `variables_template.csv` und zeigt:
- die Spaltennamen
- die ersten 5 Zeilen

## Dateien
- `app.py` – Debug-App
- `requirements.txt` – Python-Abhängigkeiten
- `variables_template.csv` – Vorlage-Datei mit Daten

## Start
```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```
