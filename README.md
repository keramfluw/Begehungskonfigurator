# CSV-Detail-Debug App

Diese App prüft im Detail die Struktur der CSV-Datei `variables_template.csv`.

Angezeigt werden:
- alle Spaltennamen (genau wie in der Datei, inkl. Leerzeichen/Sonderzeichen)
- die ersten 5 Zeilen der Daten

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
