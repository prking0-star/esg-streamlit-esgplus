import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def run_main_app():
    st.title("ESG Planning with CRREM & MEES Modelling")

    # Mock data for emissions and CRREM benchmark
    years = list(range(2025, 2036))
    emissions = [120, 110, 100, 95, 90, 85, 80, 78, 75, 73, 70]  # simulated PPM-driven emissions (kgCO2e/m²)
    crrem_limits = [100 - y*1.8 for y in range(len(years))]  # downward CRREM curve

    df = pd.DataFrame({
        "Year": years,
        "Projected Emissions (kgCO2e/m²)": emissions,
        "CRREM Limit (kgCO2e/m²)": crrem_limits
    })
    df["CRREM Status"] = df["Projected Emissions (kgCO2e/m²)"] > df["CRREM Limit (kgCO2e/m²)"]
    df["CRREM Status"] = df["CRREM Status"].apply(lambda x: "❌ Exceeds" if x else "✅ Aligned")

    st.subheader("📉 CRREM Pathway Comparison")
    st.dataframe(df)

    st.subheader("📈 Emissions vs CRREM Pathway")
    fig, ax = plt.subplots()
    ax.plot(df["Year"], df["Projected Emissions (kgCO2e/m²)"], marker='o', label="Your Emissions")
    ax.plot(df["Year"], df["CRREM Limit (kgCO2e/m²)"], marker='o', linestyle='--', label="CRREM Limit")
    ax.set_ylabel("kgCO2e per m²")
    ax.set_xlabel("Year")
    ax.set_title("CRREM Pathway")
    ax.legend()
    st.pyplot(fig)

    # MEES assumptions
    st.subheader("🏢 MEES Risk Calculator (EPC Forecasting)")

    epc_data = pd.DataFrame({
        "Building": ["Asset A", "Asset B", "Asset C"],
        "Current EPC": ["D", "F", "E"],
        "Estimated Impact (CIBSE REEB Model)": ["+1 level", "+2 levels", "+1 level"],
        "Forecast EPC (2030)": ["C", "D", "D"],
        "MEES Compliant (2030 Target = C)": ["✅", "❌", "❌"]
    })

    st.dataframe(epc_data)
