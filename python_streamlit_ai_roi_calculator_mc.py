import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config(page_title="AI ROI Calculator", layout="wide")
st.title("📈 AI ROI Calculator with Sensitivity Sliders and Monte Carlo Simulation")

st.markdown("""
This tool estimates Return on Investment (ROI) for AI initiatives by factoring in:
- Forecasted Benefits
- Accuracy, Adoption, Integration, Time to Value
- Costs: Infrastructure, Development, Ongoing Ops, etc.
- Includes Monte Carlo simulation for uncertainty analysis
""")

# --- Input Sliders ---
st.sidebar.header("🔧 Input Parameters")

# Benefits
B_f = st.sidebar.slider("Forecasted Benefits ($)", 10000, 10000000, 1000000, step=10000)
A_m = st.sidebar.slider("Accuracy Multiplier (0.0 - 1.0)", 0.0, 1.0, 0.85, step=0.01)
U_r = st.sidebar.slider("User Adoption Rate (0.0 - 1.0)", 0.0, 1.0, 0.75, step=0.01)
S_i = st.sidebar.slider("Integration Fit Score (0.0 - 1.0)", 0.0, 1.0, 0.8, step=0.01)
E_t = st.sidebar.slider("Time Efficiency Factor (0.0 - 1.0)", 0.0, 1.0, 0.9, step=0.01)

# Costs
C_i = st.sidebar.slider("Infrastructure Cost ($)", 1000, 2000000, 100000, step=1000)
C_d = st.sidebar.slider("Development & Integration Cost ($)", 1000, 5000000, 300000, step=1000)
C_o = st.sidebar.slider("Ongoing Operations Cost ($)", 1000, 2000000, 150000, step=1000)
C_c = st.sidebar.slider("Compliance & Security Cost ($)", 1000, 1000000, 100000, step=1000)
C_m = st.sidebar.slider("Maintenance & Upgrades Cost ($)", 1000, 1000000, 100000, step=1000)
C_ch = st.sidebar.slider("Change Management Cost ($)", 1000, 1000000, 50000, step=1000)

# --- ROI Calculation ---
Total_Benefits = B_f * A_m * U_r * S_i * E_t
Total_Costs = C_i + C_d + C_o + C_c + C_m + C_ch

if Total_Costs > 0:
    ROI = (Total_Benefits - Total_Costs) / Total_Costs
else:
    ROI = 0

# --- Output ---
st.subheader("📊 ROI Summary")
st.metric("Total Forecasted Benefits ($)", f"${Total_Benefits:,.2f}")
st.metric("Total Costs ($)", f"${Total_Costs:,.2f}")
st.metric("Calculated ROI", f"{ROI:.2%}")

# --- Sensitivity Table ---
st.subheader("🔍 Sensitivity Analysis (Top Drivers)")
sensitivity = {
    "Accuracy Multiplier (A_m)": A_m * B_f * U_r * S_i * E_t / A_m if A_m else 0,
    "Adoption Rate (U_r)": U_r * B_f * A_m * S_i * E_t / U_r if U_r else 0,
    "Integration Score (S_i)": S_i * B_f * A_m * U_r * E_t / S_i if S_i else 0,
    "Time Efficiency (E_t)": E_t * B_f * A_m * U_r * S_i / E_t if E_t else 0,
    "Development Cost (C_d)": C_d,
    "Maintenance Cost (C_m)": C_m,
}

sorted_sens = sorted(sensitivity.items(), key=lambda x: -abs(x[1]))

for name, value in sorted_sens:
    st.write(f"**{name}**: ${value:,.2f}")

# --- Monte Carlo Simulation ---
st.subheader("🎲 Monte Carlo Simulation")
n_sim = st.slider("Number of Simulations", 100, 10000, 1000, step=100)

# Define standard deviations (10% for example)
sd_pct = 0.10

np.random.seed(42)
benefits_samples = np.random.normal(B_f, B_f * sd_pct, n_sim)
accuracy_samples = np.random.normal(A_m, A_m * sd_pct, n_sim)
adoption_samples = np.random.normal(U_r, U_r * sd_pct, n_sim)
integration_samples = np.random.normal(S_i, S_i * sd_pct, n_sim)
time_efficiency_samples = np.random.normal(E_t, E_t * sd_pct, n_sim)

costs_samples = np.random.normal(Total_Costs, Total_Costs * sd_pct, n_sim)

roi_samples = ((benefits_samples * accuracy_samples * adoption_samples * integration_samples * time_efficiency_samples) - costs_samples) / costs_samples
roi_samples = np.nan_to_num(roi_samples)

st.write(f"**Mean ROI:** {np.mean(roi_samples):.2%}")
st.write(f"**5th Percentile ROI:** {np.percentile(roi_samples, 5):.2%}")
st.write(f"**95th Percentile ROI:** {np.percentile(roi_samples, 95):.2%}")

# --- ROI Histogram ---
st.subheader("📉 ROI Distribution")
st.bar_chart(pd.DataFrame(roi_samples, columns=["Simulated ROI"]))
