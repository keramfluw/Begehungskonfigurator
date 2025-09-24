import streamlit as st
import pandas as pd
import numpy as np
import io
from datetime import datetime
import plotly.express as px

st.set_page_config(page_title="Wirtschaftlichkeits-Konfigurator", layout="wide")

@st.cache_data
def load_variables(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    # Ensure expected columns exist
    expected = ["Variant","Activity","Required_Competency","Responsible","Time_h","Baseline_Cost_EUR",
                "Rationale","Notes","Include_Default","Category","Quantity_Default","Hourly_Rate_Default",
                "Suggested_Sales_EUR"]
    for col in expected:
        if col not in df.columns:
            df[col] = np.nan
    # Fill sensible defaults
    df["Include_Default"] = df["Include_Default"].fillna(True).astype(bool)
    df["Quantity_Default"] = df["Quantity_Default"].fillna(1.0).astype(float)
    df["Hourly_Rate_Default"] = df["Hourly_Rate_Default"].fillna(75.0).astype(float)
    df["Time_h"] = df["Time_h"].fillna(0.0).astype(float)
    df["Baseline_Cost_EUR"] = df["Baseline_Cost_EUR"].fillna(0.0).astype(float)
    df["Suggested_Sales_EUR"] = df["Suggested_Sales_EUR"].fillna(
        (df["Time_h"] * df["Hourly_Rate_Default"]).round(2)
    )
    df["Variant"] = df["Variant"].fillna("Unbekannt")
    df["Activity"] = df["Activity"].fillna("Position")
    df["Category"] = df["Category"].fillna("Labor")
    return df

def currency(x: float) -> str:
    try:
        return f"{x:,.2f} €".replace(",", "X").replace(".", ",").replace("X",".")
    except Exception:
        return "-"

st.title("⚙️ Wirtschaftlichkeits‑Konfigurator (Vertrieb)")
st.caption("Version {v} • Erstellt: {dt}".format(v="0.1", dt=datetime.now().strftime("%d.%m.%Y %H:%M")))

with st.sidebar:
    st.header("🔧 Globale Annahmen")
    variables_file = st.file_uploader("Variablen‑CSV laden", type=["csv"], accept_multiple_files=False)
    if variables_file is not None:
        df_vars = load_variables(variables_file)
    else:
        df_vars = load_variables("variables_template.csv")

    st.subheader("Kosten & Zuschläge")
    default_hourly = float(np.nanmedian(df_vars["Hourly_Rate_Default"])) if not df_vars.empty else 75.0
    hourly_rate = st.number_input("Standard‑Stundensatz (€/h)", min_value=0.0, value=default_hourly, step=5.0)
    overhead_pct = st.number_input("Gemeinkosten/Overhead (%)", min_value=0.0, value=15.0, step=1.0)
    ext_costs = st.number_input("Externe Kosten (gesamt, €)", min_value=0.0, value=0.0, step=50.0)
    materials_costs = st.number_input("Materialkosten (gesamt, €)", min_value=0.0, value=0.0, step=50.0)

    st.subheader("Preisgestaltung")
    markup_pct = st.number_input("Aufschlag auf Vollkosten (%)", min_value=0.0, value=25.0, step=1.0)
    discount_pct = st.number_input("Rabatt/Skonto (%)", min_value=0.0, value=0.0, step=0.5)

# Auswahl der Varianten
variants = sorted(df_vars["Variant"].dropna().unique().tolist())
sel_variants = st.multiselect("Varianten auswählen", variants, default=variants[:1])

# Filter DataFrame
work_df = df_vars[df_vars["Variant"].isin(sel_variants)].copy()

st.markdown("### 🔩 Positionen")

edits = []
totals = []

for v in sel_variants:
    subset = work_df[work_df["Variant"] == v].copy().reset_index(drop=True)
    with st.expander(f"{v} • {len(subset)} Positionen", expanded=True):
        for i, row in subset.iterrows():
            key = f"{v}-{i}"
            cols = st.columns([0.05, 0.35, 0.12, 0.12, 0.12, 0.12, 0.12])
            include = cols[0].checkbox("", value=bool(row.get("Include_Default", True)), key=key+"-inc")
            cols[1].markdown(f"**{row['Activity']}**")
            time_h = cols[2].number_input("Zeit (h)", min_value=0.0, value=float(row["Time_h"]), step=0.25, key=key+"-time")
            qty = cols[3].number_input("Menge", min_value=0.0, value=float(row.get("Quantity_Default", 1.0)), step=1.0, key=key+"-qty")
            rate = cols[4].number_input("€/h", min_value=0.0, value=float(hourly_rate if np.isnan(row.get("Hourly_Rate_Default", np.nan)) else row.get("Hourly_Rate_Default")), step=5.0, key=key+"-rate")
            base_cost = cols[5].number_input("Basis‑Kosten (€)", min_value=0.0, value=float(row.get("Baseline_Cost_EUR", 0.0)), step=10.0, key=key+"-base")
            line_cost = time_h * rate * qty
            cols[6].markdown(f"**{currency(line_cost)}**")
            edits.append({
                "Variant": v,
                "Activity": row["Activity"],
                "Include": include,
                "Time_h": time_h,
                "Qty": qty,
                "Rate_EUR_h": rate,
                "Baseline_Cost_EUR": base_cost,
                "Calc_Labor_Cost_EUR": line_cost,
                "Notes": row.get("Notes", ""),
                "Rationale": row.get("Rationale", ""),
            })
    # Totals per variant
    if subset.shape[0] > 0:
        pass

cfg_df = pd.DataFrame(edits)

if cfg_df.empty:
    st.warning("Bitte mindestens eine Variante und Position auswählen.")
    st.stop()

# Kostenrechnung
cfg_df["Eff_Cost_EUR"] = cfg_df[["Baseline_Cost_EUR","Calc_Labor_Cost_EUR"]].max(axis=1)
cfg_df["Eff_Cost_EUR"] = np.where(cfg_df["Include"], cfg_df["Eff_Cost_EUR"], 0.0)

direct_costs = cfg_df["Eff_Cost_EUR"].sum()
overhead = direct_costs * (overhead_pct/100.0)
full_cost = direct_costs + overhead + ext_costs + materials_costs
list_price = full_cost * (1.0 + markup_pct/100.0)
offer_price = list_price * (1.0 - discount_pct/100.0)
profit = offer_price - full_cost
margin_pct = (profit/offer_price*100.0) if offer_price > 0 else 0.0

st.markdown("### 📊 Ergebnisübersicht")

kpi_cols = st.columns(6)
kpi_cols[0].metric("Direkte Kosten", currency(direct_costs))
kpi_cols[1].metric("Overhead", currency(overhead))
kpi_cols[2].metric("Vollkosten", currency(full_cost))
kpi_cols[3].metric("Listenpreis", currency(list_price))
kpi_cols[4].metric("Angebotspreis (nach Rabatt)", currency(offer_price))
kpi_cols[5].metric("Deckungsbeitrag", f"{currency(profit)} ({margin_pct:,.1f} %)")

# Chart Kosten vs Preis
chart_df = pd.DataFrame({
    "Komponente": ["Direkte Kosten", "Overhead", "Externe Kosten", "Materialkosten", "Vollkosten", "Angebotspreis"],
    "EUR": [direct_costs, overhead, ext_costs, materials_costs, full_cost, offer_price]
})
fig = px.bar(chart_df, x="Komponente", y="EUR", text="EUR", title="Kostenstruktur & Angebotspreis")
st.plotly_chart(fig, use_container_width=True)

# Tabellarische Ansicht ausgewählter Positionen
st.markdown("### 📄 Detailtabelle (ausgewählte Positionen)")
show_df = cfg_df[cfg_df["Include"]].copy()
show_df["Zeilenkosten (€)"] = show_df["Eff_Cost_EUR"].round(2)
show_cols = ["Variant","Activity","Time_h","Qty","Rate_EUR_h","Baseline_Cost_EUR","Zeilenkosten (€)","Notes"]
st.dataframe(show_df[show_cols], use_container_width=True)

# Export
st.markdown("### ⬇️ Exporte")
def to_bytes_csv(df: pd.DataFrame) -> bytes:
    return df.to_csv(index=False).encode("utf-8")

def to_bytes_excel(sheets: dict) -> bytes:
    buf = io.BytesIO()
    with pd.ExcelWriter(buf, engine="xlsxwriter") as xw:
        for name, d in sheets.items():
            d.to_excel(xw, sheet_name=name[:31], index=False)
    return buf.getvalue()

export_cfg = cfg_df.copy()
export_cfg["Calc_Timestamp"] = datetime.now().isoformat()

c1, c2 = st.columns(2)
c1.download_button("CSV exportieren", data=to_bytes_csv(export_cfg), file_name="konfigurator_export.csv", mime="text/csv")
c2.download_button("Excel exportieren", data=to_bytes_excel({
    "Konfiguration": export_cfg,
    "Kostenübersicht": pd.DataFrame({
        "Direkte Kosten": [direct_costs],
        "Overhead": [overhead],
        "Externe Kosten": [ext_costs],
        "Materialkosten": [materials_costs],
        "Vollkosten": [full_cost],
        "Listenpreis": [list_price],
        "Angebotspreis": [offer_price],
        "Deckungsbeitrag": [profit],
        "Marge (%)": [margin_pct],
        "Rabatt (%)": [discount_pct],
        "Aufschlag (%)": [markup_pct],
    })
}), file_name="konfigurator_export.xlsx", mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

st.info("Tipp: Passen Sie **variables_template.csv** an (z. B. zusätzliche Kategorien, Materialpositionen, Fremdleistungen). Laden Sie die Datei oben neu, um mit Ihren Daten zu rechnen.")
