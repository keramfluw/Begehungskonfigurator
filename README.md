# Robuste Varianten-Auswahl App

Diese Version lädt die Datei `variables_template.csv` und erlaubt die Auswahl der Spalte `Variant`.  
Sie ist robuster implementiert:
- Leere Werte (NaN) werden entfernt
- Alle Werte werden als String behandelt
- Bei Fehlern werden Hinweise angezeigt, statt dass die App abstürzt

## Dateien
- `app.py` – Robuste Varianten-Auswahl
- `requirements.txt` – Abhängigkeiten
- `variables_template.csv` – Testdatei

## Start
```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```
