import streamlit as st
from streamlit_extras.switch_page_button import switch_page

# Page config
st.set_page_config(page_title="AutoAnalytica", page_icon="🔍", layout="wide")

# MAIN HERO SECTION
st.title("Welcome to AutoAnalytica! 🔍")
st.markdown(
    """
    **Your AI-powered data partner — Upload. Explore. Predict. Decide.**  
    Upload your data, run instant analysis, forecast trends, and get AI-generated insights — all in one place.  
    """
)

# BUTTON NAVIGATION
col1, col2 = st.columns(2)

with col1:
    if st.button("📤 Upload Your Dataset", use_container_width=True):
        switch_page("Upload Data")  # Must match the page title/file name in `pages/`

with col2:
    if st.button("📊 Try Demo Data", use_container_width=True):
        switch_page("AutoEDA")  # Must match the page title/file name in `pages/`

st.markdown("---")

# -------------------
# HOW IT WORKS
# -------------------
st.subheader("⚡ How It Works")
steps = [
    "1️⃣ **Upload or Connect Data** — CSV, Excel, SQL, or Google Sheets.",
    "2️⃣ **Analyze & Get Insights** — AutoEDA, visualizations, and key metrics.",
    "3️⃣ **Download or Share Reports** — PDF, PNG, or interactive dashboards."
]
for step in steps:
    st.markdown(step)

st.markdown("---")

# FEATURES
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

# FOOTER
st.markdown(
    """
    ---
    Built with ❤️ using Streamlit | [GitHub Repo](https://github.com/ummessh/AutoAnalytica) | [Documentation](#)
    """,
    unsafe_allow_html=True
)
