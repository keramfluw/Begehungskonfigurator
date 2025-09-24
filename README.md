# Minimal-Version Wirtschaftlichkeits-Konfigurator

Dies ist eine stark vereinfachte Version der App. Sie dient nur zum Test, ob `streamlit` bei dir läuft.

## Dateien

- `app.py` – Minimal-App
- `requirements.txt` – Python-Abhängigkeiten
- `variables_template.csv` – Vorlage mit den Variablen

## Start

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

## Nutzung

1. CSV-Datei `variables_template.csv` liegt im Verzeichnis.
2. Starte die App, wähle Varianten und sieh die Tabelle und Gesamtsumme der Kosten.
