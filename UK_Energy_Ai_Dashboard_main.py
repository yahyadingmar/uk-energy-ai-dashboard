
import streamlit as st
import pandas as pd
import datetime

# Set up layout
st.set_page_config(page_title="UK Energy AI Dashboard", layout="wide", initial_sidebar_state="expanded")

# Apply dark theme styling manually
st.markdown("""
    <style>
    body { background-color: #0e1117; color: #fafafa; }
    .reportview-container .markdown-text-container { color: #fafafa; }
    .stDataFrame { background-color: #1e1e1e; color: #ffffff; }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("🔌 UK Gas & Power Market Intelligence Dashboard")
st.caption("Powered by Streamlit + OpenAI | Live Data • Curve Analysis • Commentary • Chat")

# Date
today = datetime.date.today()
st.sidebar.markdown(f"**Date:** {today.strftime('%A, %d %B %Y')}")

# Sidebar Navigation
page = st.sidebar.radio("Navigate", [
    "📊 Market Prices",
    "🗞️ Commentary & Summaries",
    "⚡ Renewables & Flows",
    "🤖 Chat Assistant"
])

if page == "📊 Market Prices":
    st.header("📊 Gas & Power Forward Curves")
    # Placeholder DataFrame
    df = pd.DataFrame({
        "Contract": ["Summer-25", "Winter-25", "Summer-26"],
        "NBP Gas (p/th)": [86.5, 94.1, 81.2],
        "UK Power (£/MWh)": [74.6, 85.9, 71.3]
    })
    st.dataframe(df, use_container_width=True)

    st.subheader("📅 Week-on-Week Comparison")
    comp = pd.DataFrame({
        "Period": ["Week Prior", "Last Week", "Current Week"],
        "NBP Gas Avg (p/th)": [82.3, 84.5, 86.1],
        "UK Power Avg (£/MWh)": [69.8, 71.5, 73.2]
    })
    st.dataframe(comp, use_container_width=True)

    st.subheader("📌 Key Price Drivers")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**📈 Bullish Drivers (Gas):**\n- LNG outage risk\n- Low wind gen\n- Geopolitical tensions")
        st.markdown("**📈 Bullish Drivers (Power):**\n- Low nuclear output\n- High demand forecast\n- Rising EUA prices")
    with col2:
        st.markdown("**📉 Bearish Drivers (Gas):**\n- Strong Norwegian flows\n- Soft demand outlook\n- Flexible EU storage policy")
        st.markdown("**📉 Bearish Drivers (Power):**\n- High wind output\n- Mild temperatures\n- Strong imports")

elif page == "🗞️ Commentary & Summaries":
    st.header("🗞️ Upload Commentary (PDF or Text)")
    uploaded_file = st.file_uploader("Upload your market report", type=["pdf", "txt"])
    if uploaded_file:
        st.success("File received. AI summary coming soon...")
        st.info("🔍 AI summary and market impact analysis will appear here.")

elif page == "⚡ Renewables & Flows":
    st.header("⚡ Renewable Output + System Flows")
    st.markdown("- Wind output (past 7 days): Chart incoming\n- Solar trend vs seasonal avg: Coming soon\n- National Gas system flows\n- Norwegian maintenance status")
    st.info("This module will visualize renewables and key gas flows using historical + live data.")

elif page == "🤖 Chat Assistant":
    st.header("🤖 Market Intelligence Chat")
    st.markdown("Ask anything about prices, drivers, system status, or storage.")
    st.chat_input("Ask a question...")
    st.info("Assistant will use historical commentary + real-time data context.")

st.markdown("---")
st.caption("© 2025 UK Energy AI Dashboard – Built with Streamlit + OpenAI")
