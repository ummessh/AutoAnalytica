# 4 DataChatbot
# 4 DataChatbot
import streamlit as st
import pandas as pd
import os
from pandasai import SmartDataframe
from pandasai.llm.openai import OpenAI
from dotenv import load_dotenv

st.title("🤖 GPT-Powered Chatbot for Your Data")

# Load env key
load_dotenv()
openai_key = os.getenv("OPENAI_API_KEY")

if not openai_key:
    st.error("❌ OpenAI API key not found. Add it to .env file.")
    st.stop()

# Load cleaned dataframe
if "cleaned_df" not in st.session_state:
    st.warning("⚠️ No cleaned data found. Please upload and clean a dataset first.")
    st.stop()

df = st.session_state["cleaned_df"]
st.dataframe(df.head(), use_container_width=True)

# Setup GPT with PandasAI
llm = OpenAI(api_token=openai_key)
sdf = SmartDataframe(df, config={"llm": llm})

# User input
question = st.text_input("💬 Ask your data (e.g., 'What is the average revenue by region?')")

if question:
    with st.spinner("Thinking... 🧠"):
        try:
            response = sdf.chat(question)
            st.success("✅ Here's what I found:")
            st.write(response)
        except Exception as e:
            st.error(f"Error: {e}")
