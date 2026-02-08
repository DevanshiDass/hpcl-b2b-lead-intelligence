import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="HPCL Executive Dashboard",
    layout="centered"
)

# ---------------- HEADER ----------------
st.title("HPCL Executive Dashboard")
st.caption("Management View · Lead Intelligence Summary")
st.divider()

# ---------------- KPI METRICS ----------------
st.subheader("Key Performance Indicators")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Leads Generated (Weekly)", "42", "+8")
col2.metric("Leads Accepted", "18", "+3")
col3.metric("Leads Converted", "7", "+2")
col4.metric("Conversion Rate", "16.6%", "+1.4%")

st.caption("Week-over-week comparison based on sales updates")

st.divider()

# ---------------- LEAD FUNNEL ----------------
st.subheader("Lead Funnel Overview")

st.markdown("""
- **Discovered:** 42  
- **Qualified by System:** 31  
- **Accepted by Sales:** 18  
- **Converted to Orders:** 7  
""")

st.info(
    "Biggest drop observed between *System Qualified* and *Sales Accepted*. "
    "Recommendation: improve lead prioritization and urgency signaling."
)

st.divider()

# ---------------- PRODUCT INTELLIGENCE ----------------
st.subheader("Product Intelligence")

col1, col2 = st.columns(2)

with col1:
    st.markdown("**Top Products by Lead Volume**")
    st.write("- Furnace Oil (FO) — 38%")
    st.write("- High Speed Diesel (HSD) — 31%")
    st.write("- Bitumen — 24%")
    st.write("- Marine Fuels — 7%")

with col2:
    st.markdown("**High Conversion Products**")
    st.write("- Bitumen — 26% conversion")
    st.write("- Furnace Oil — 18% conversion")
    st.write("- HSD — 12% conversion")

st.success(
    "Insight: Bitumen leads have lower volume but highest conversion. "
    "Opportunity for focused infrastructure outreach."
)

st.divider()

# ---------------- SECTOR INTELLIGENCE ----------------
st.subheader("Sector-wise Demand Signals")

st.markdown("""
- **Infrastructure & Roads** — High urgency, fast closures  
- **Power & Captive Plants** — High volume, medium conversion  
- **Chemicals & Manufacturing** — Stable, long-cycle deals  
""")

st.info(
    "Infrastructure projects show strongest near-term revenue potential. "
    "Recommend regional sales push aligned with government tenders."
)

st.divider()

# ---------------- REGIONAL INTELLIGENCE ----------------
st.subheader("Regional Performance")

col1, col2 = st.columns(2)

with col1:
    st.markdown("**Top Lead Generating Regions**")
    st.write("- Chhattisgarh")
    st.write("- Maharashtra")
    st.write("- Odisha")

with col2:
    st.markdown("**High Conversion Regions**")
    st.write("- Maharashtra")
    st.write("- Gujarat")
    st.write("- Rajasthan")

st.success(
    "Insight: Chhattisgarh generates volume but conversion lags. "
    "Sales enablement and faster follow-up recommended."
)

st.divider()

# ---------------- ACTIONABLE RECOMMENDATIONS ----------------
st.subheader("Executive Recommendations")

st.markdown("""
1. **Prioritize Bitumen and Infrastructure-led opportunities**  
2. **Improve sales acceptance rate with clearer urgency tagging**  
3. **Strengthen follow-up in high-volume regions with low conversion**  
4. **Use confidence score thresholds to reduce sales overload**  
""")

st.info(
    "All insights are derived from public signal intelligence, "
    "system inference, and sales officer status updates."
)
