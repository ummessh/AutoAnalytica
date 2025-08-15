import streamlit as st
import os

# Page config
st.set_page_config(page_title="AutoAnalytica", page_icon="🔍", layout="wide")

# Hide sidebar (optional)
hide_sidebar_style = """
    <style>
        [data-testid="stSidebar"] { display: none; }
    </style>
"""
st.markdown(hide_sidebar_style, unsafe_allow_html=True)

# --- Handle navigation state ---
if "nav_target" not in st.session_state:
    st.session_state.nav_target = None

# Redirect if a target page is set
if st.session_state.nav_target:
    target_file = f"pages/{st.session_state.nav_target}.py"
    if os.path.exists(target_file):
        with open(target_file, "r", encoding="utf-8") as f:
            code = f.read()
        exec(code, globals())
        st.stop()
    else:
        st.error(f"Page '{st.session_state.nav_target}' not found.")
        st.session_state.nav_target = None

# --- Main Hero Section ---
st.title("Welcome to AutoAnalytica! 🔍")
st.markdown("""
**Your AI-powered data partner — Upload. Explore. Predict. Decide.**  
Upload your data, run instant analysis, forecast trends, and get AI-generated insights — all in one place.
""")

# Navigation buttons
col1, col2 = st.columns(2)

with col1:
    if st.button("📤 Upload Your Dataset"):
        st.session_state.nav_target = "Upload Data"
        st.experimental_rerun()

with col2:
    if st.button("📊 Try Demo Data"):
        st.session_state.nav_target = "AutoEDA"
        st.experimental_rerun()

st.markdown("---")

# How it works
st.subheader("⚡ How It Works")
steps = [
    "1️⃣ **Upload or Connect Data** — CSV, Excel, SQL, or Google Sheets.",
    "2️⃣ **Analyze & Get Insights** — AutoEDA, visualizations, and key metrics.",
    "3️⃣ **Download or Share Reports** — PDF, PNG, or interactive dashboards."
]
for step in steps:
    st.markdown(step)

st.markdown("---")

# Features
st.subheader("✨ Key Features")
feature_cols = st.columns(4)
features = [
    ("📈 AutoEDA", "Instantly explore trends & patterns."),
    ("🤖 AI Insights", "AI-generated summaries & explanations."),
    ("💬 Data Chatbot", "Ask questions, get answers instantly."),
    ("📅 Strategy Module", "Forecast & plan your next move.")
]
for i, (title, desc) in enumerate(features):
    with feature_cols[i]:
        st.markdown(f"**{title}**\n\n{desc}")

st.markdown("---")

# Footer
st.markdown("""
---
Built with ❤️ using Streamlit | [GitHub Repo](https://github.com/ummessh/AutoAnalytica) | [Documentation](#)
""", unsafe_allow_html=True)
