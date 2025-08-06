import streamlit as st
import pandas as pd
import os
from openai import OpenAI

st.title("🧠 AI-Generated Data Insights")

if "cleaned_df" not in st.session_state:
    st.warning("⚠️ No cleaned data found. Please upload and clean a dataset first.")
    st.stop()

df = st.session_state["cleaned_df"]
df = df.convert_dtypes()
df = df.infer_objects()

# 🔐 Load API key from environment
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@st.cache_data(show_spinner=True)
def generate_gpt_insight(data: pd.DataFrame) -> str:
    summary = data.describe(include='all').to_string()

    numeric_df = data.select_dtypes(include='number')
    if not numeric_df.empty:
        correlation = numeric_df.corr().to_string()
    else:
        correlation = "No numeric columns to compute correlation."

    prompt = f"""
You are a senior data analyst. Analyze the following dataset based on its summary and correlation table.
Find 3-5 key insights that would help a business make decisions.

### Summary Stats:
{summary}

### Correlation Matrix:
{correlation}

Return your response in bullet points. Use simple, professional language.
"""

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful data science assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.4
    )

    return response.choices[0].message.content

if st.button("🔍 Generate Insights with AI"):
    with st.spinner("Analyzing data using GPT..."):
        insights = generate_gpt_insight(df)
        st.subheader("💡 Key Insights:")
        st.markdown(insights)
