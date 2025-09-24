# CSV-Lese-Test App

Diese App prüft, ob die Datei `variables_template.csv` mit Pandas korrekt geladen werden kann.

Angezeigt werden:
- Die Spaltennamen der CSV
- Die ersten 5 Zeilen als Tabelle

## Dateien
- `app.py` – Lese-Test-App
- `requirements.txt` – Abhängigkeiten
- `variables_template.csv` – Testdatei

## Start
```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```
