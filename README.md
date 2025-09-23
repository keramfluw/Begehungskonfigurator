
# Qrauts – Minimal App (Testversion)

Dies ist eine abgespeckte Version der Angebots-/Baustein-App, um die Grundfunktionalität sicherzustellen.

## Funktionen
- Laden des Katalogs aus `catalog.csv` (falls vorhanden), sonst Dummy-Beispieldaten
- Editierbare Tabelle (Tätigkeit, Stunden, Satz, VK)
- Automatische Berechnung von Kosten, Umsatz und Deckungsbeitrag
- Minimaler, stabiler Aufbau (zum Testen der Umgebung)

## Start (lokal)
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Dateien
- `app.py` – Haupt-App (Streamlit)
- `requirements.txt` – Python-Pakete (minimal)
- `catalog.csv` – Optional, kann Bausteine enthalten (Struktur: variant, activity, default_hours, default_internal_rate, default_sale_price)
