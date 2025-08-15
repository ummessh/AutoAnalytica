import streamlit as st

# Page config
st.set_page_config(page_title="AutoAnalytica", page_icon="🔍", layout="wide")

# Hero section
st.title("Welcome to AutoAnalytica! 🔍")
st.markdown("""
**Your AI-powered data partner — Upload. Explore. Predict. Decide.**  
Upload your data, run instant analysis, forecast trends, and get AI-generated insights — all in one place.
""")

# Navigation buttons
col1, col2 = st.columns(2)

with col1:
    if st.button("📤 Upload Your Dataset"):
        st.switch_page("pages/1_Upload_Data.py")  # match your actual file name

with col2:
    if st.button("📊 Try Demo Data"):
        st.switch_page("pages/2_AutoEDA.py")  # match your actual file name

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
