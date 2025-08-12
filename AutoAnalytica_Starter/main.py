import streamlit as st

# Page config
st.set_page_config(page_title="AutoAnalytica", page_icon="🔍", layout="wide")

# -------------------
# MAIN HERO SECTION
# -------------------
st.title("Welcome to AutoAnalytica! 🔍")
st.markdown(
    """
    **Your AI-powered data partner — Upload. Explore. Predict. Decide.**  
    Upload your data, run instant analysis, forecast trends, and get AI-generated insights — all in one place.  
    """
)

# -------------------
# BUTTON NAVIGATION
# -------------------
# Map of Button Label -> Page Name (matches sidebar label from page title)
page_links = {
    "📤 Upload Your Dataset": "Upload Data",
    "📊 Try Demo Data": "AutoEDA"
}

col1, col2 = st.columns(2)

for i, (label, page_name) in enumerate(page_links.items()):
    button_html = f"""
    <a href="./{page_name.replace(' ', '%20')}" target="_self">
        <button style="
            background-color:{'#4CAF50' if i == 0 else '#2196F3'};
            color:white;
            padding:10px 18px;
            border:none;
            border-radius:6px;
            font-size:16px;
            cursor:pointer;
        ">
            {label}
        </button>
    </a>
    """
    if i == 0:
        col1.markdown(button_html, unsafe_allow_html=True)
    else:
        col2.markdown(button_html, unsafe_allow_html=True)

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

# -------------------
# FEATURES
# -------------------
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

# -------------------
# FOOTER
# -------------------
st.markdown(
    """
    ---
    Built with ❤️ using Streamlit | [GitHub Repo](https://github.com/) | [Documentation](#)
    """,
    unsafe_allow_html=True
)
