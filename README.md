# Wirtschaftlichkeits‑Konfigurator (Vertrieb)

Dieser Prototyp erstellt aus der bereitgestellten **RACI_Matrix_Energiechecks.xlsx** eine konfigurierbare App zur Kalkulation von Leistungen (Varianten & Tätigkeiten).

## Dateien

- `app.py` – Streamlit‑App
- `requirements.txt` – Python‑Abhängigkeiten
- `README.md` – diese Anleitung
- `variables_template.csv` – aus dem Excel abgeleitete Vorlage, die Sie anpassen können

## Installation

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

## Nutzung

1. Öffnen Sie die App in Ihrem Browser (lokal typischerweise http://localhost:8501).
2. Laden Sie optional eine angepasste `variables_template.csv` über die Sidebar hoch.
3. Wählen Sie **Varianten** aus und konfigurieren Sie Positionen (Zeit, Menge, €/h, Basis‑Kosten).
4. Passen Sie globale Annahmen an: Stundensatz, Overhead, externe Kosten, Material, Aufschlag, Rabatt.
5. Exportieren Sie Ergebnisse als **CSV** oder **Excel**.

## CSV‑Struktur (`variables_template.csv`)

Spalten:
- `Variant` – Variantenbezeichnung (z. B. „V1 - Basis-Check“)
- `Activity` – Tätigkeit/Position
- `Required_Competency` – benötigte Qualifikation
- `Responsible` – intern/extern etc.
- `Time_h` – Richtzeit je Position
- `Baseline_Cost_EUR` – vorhandene Kostenschätzung (optional)
- `Rationale` – fachliche Begründung
- `Notes` – Bemerkungen
- `Include_Default` – `TRUE`/`FALSE`
- `Category` – z. B. Labor/Material/Extern (optional)
- `Quantity_Default` – Startmenge
- `Hourly_Rate_Default` – Start‑Stundensatz für diese Position
- `Suggested_Sales_EUR` – optionaler Start‑Verkaufspreis (informativ)

> **Hinweis:** Die App berechnet die Zeilenkosten als `max(Baseline_Cost_EUR, Time_h * Hourly_Rate * Menge)` wenn die Position aktiviert ist.

## Datenherkunft

Die Vorlage wurde aus dem Blatt **Matrix** der Datei `RACI_Matrix_Energiechecks.xlsx` generiert (Stand: 24.09.2025 13:45). Die Summen je Variante können Sie im Blatt **Summen je Variante** der Excel prüfen.

## Anpassungen / Ideen

- Zusätzliche CSVs (z. B. `materials.csv`, `externals.csv`) für feinere Kategorien.
- Deckungsbeitrags‑ und Break‑Even‑Visualisierung je Variante.
- Rollen‑/Qualifikationsfilter und automatische Ressourcenkosten pro Kompetenz.
- Mehrsprachigkeit (DE/EN) und Angebots‑PDF (falls gewünscht).
