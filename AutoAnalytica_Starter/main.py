import streamlit as st
from PIL import Image

# Page Config
st.set_page_config(page_title="AutoAnalytica", page_icon="🔍", layout="wide")

# Hero Section
st.title("Welcome to AutoAnalytica! 🔍")
st.markdown(
    """
    **Your AI-powered data partner — Upload. Explore. Predict. Decide.**  
    Upload your data, run instant analysis, forecast trends, and get AI-generated insights — all in one place.  
    """
)

# Action Buttons
col1, col2 = st.columns(2)
with col1:
    if st.button("📤 Upload Your Dataset"):
        st.switch_page("pages/UploadData.py")  # Adjust path if needed
with col2:
    if st.button("📊 Try Demo Data"):
        st.session_state['demo_data'] = True
        st.switch_page("pages/AutoEDA.py")  # Adjust path if needed

st.markdown("---")

# How It Works
st.subheader("⚡ How It Works")
steps = [
    "1️⃣ **Upload or Connect Data** — CSV, Excel, SQL, or Google Sheets.",
    "2️⃣ **Analyze & Get Insights** — AutoEDA, visualizations, and key metrics.",
    "3️⃣ **Download or Share Reports** — PDF, PNG, or interactive dashboards."
]
for step in steps:
    st.markdown(step)

st.markdown("---")

# Feature Cards
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

# Demo Section
st.subheader("🎥 See AutoAnalytica in Action")
demo_gif = "demo.gif"  # Replace with actual file path
try:
    st.image(demo_gif, caption="Your data. Your insights. Instantly.")
except:
    st.info("Demo video/GIF coming soon!")

# Footer
st.markdown(
    """
    ---
    Built with ❤️ using Streamlit | [GitHub Repo](https://github.com/) | [Documentation](#)
    """
)
