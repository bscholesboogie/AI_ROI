# Can be run in Python locally or in Colab
# Can also be run on Streamlit Cloud (https://streamlit.io/)

import streamlit as st

st.set_page_config(page_title="AI ROI Calculator", layout="centered")

st.title("🤖 AI ROI Calculator")

st.subheader("📥 Input Benefits")
labor_savings = st.number_input("Labor Cost Savings ($)", min_value=0)
revenue_uplift = st.number_input("Revenue Uplift ($)", min_value=0)
productivity_gains = st.number_input("Productivity Gains ($)", min_value=0)
error_reduction = st.number_input("Error Reduction Savings ($)", min_value=0)
time_to_delivery_savings = st.number_input("Time to Delivery Savings ($)", min_value=0)
strategic_value = st.number_input("Strategic Value ($)", min_value=0)

st.subheader("📤 Input Costs")
model_fees = st.number_input("Model/API Fees ($)", min_value=0)
infra_costs = st.number_input("Infrastructure Costs ($)", min_value=0)
dev_integration = st.number_input("Development & Integration ($)", min_value=0)
fine_tuning = st.number_input("Fine-tuning / Customization ($)", min_value=0)
personnel_costs = st.number_input("Personnel Costs ($)", min_value=0)
compliance_costs = st.number_input("Security & Compliance ($)", min_value=0)
maintenance_costs = st.number_input("Ongoing Maintenance ($)", min_value=0)
change_mgmt = st.number_input("Change Management ($)", min_value=0)

# Calculations
total_benefits = sum([
    labor_savings, revenue_uplift, productivity_gains,
    error_reduction, time_to_delivery_savings, strategic_value
])

total_investment = sum([
    model_fees, infra_costs, dev_integration, fine_tuning,
    personnel_costs, compliance_costs, maintenance_costs, change_mgmt
])

roi_percent = ((total_benefits - total_investment) / total_investment) * 100 if total_investment else float('inf')
payback_months = total_investment / (total_benefits / 12) if total_benefits else float('inf')

st.subheader("📊 Results")
st.metric("Total Annualized Benefits", f"${total_benefits:,.2f}")
st.metric("Total Investment", f"${total_investment:,.2f}")
st.metric("ROI (%)", f"{roi_percent:.2f}%")
st.metric("Payback Period", f"{payback_months:.1f} months")

