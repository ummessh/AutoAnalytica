import streamlit as st

# Page config
st.set_page_config(page_title="AutoAnalytica", page_icon="🔍", layout="wide")

# Hero Section
st.title("Welcome to AutoAnalytica! 🔍")
st.markdown(
    """
    **Your AI-powered data partner — Upload. Explore. Predict. Decide.**  
    Upload your data, run instant analysis, forecast trends, and get AI-generated insights — all in one place.  
    """
)

# Action Buttons (links instead of switch_page)
col1, col2 = st.columns(2)

with col1:
    st.markdown(
        """
        <a href="./UploadData" target="_self">
            <button style="background-color:#4CAF50; color:white; padding:10px 18px; border:none; border-radius:6px; font-size:16px; cursor:pointer;">
                📤 Upload Your Dataset
            </button>
        </a>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        """
        <a href="./AutoEDA" target="_self">
            <button style="background-color:#2196F3; color:white; padding:10px 18px; border:none; border-radius:6px; font-size:16px; cursor:pointer;">
                📊 Try Demo Data
            </button>
        </a>
        """,
        unsafe_allow_html=True
    )

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

# Footer
st.markdown(
    """
    ---
    Built with ❤️ using Streamlit | [GitHub Repo](https://github.com/) | [Documentation](#)
    """,
    unsafe_allow_html=True
)
