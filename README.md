# Filesystem-Debug App

Diese App zeigt:
- Alle Dateien im aktuellen Verzeichnis
- Ob `variables_template.csv` vorhanden ist
- Falls vorhanden: die ersten 500 Zeichen des Inhalts

## Dateien
- `app.py` – Filesystem-Debug
- `requirements.txt` – Abhängigkeiten
- `variables_template.csv` – Testdatei (falls vorhanden)

## Start
```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```
