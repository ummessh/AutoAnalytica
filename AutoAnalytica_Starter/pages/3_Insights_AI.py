import streamlit as st
import pandas as pd
import os
import time
from openai import OpenAI, RateLimitError

st.title("🧠 AI-Generated Data Insights")

if "cleaned_df" not in st.session_state:
    st.warning("⚠️ No cleaned data found. Please upload and clean a dataset first.")
    st.stop()

df = st.session_state["cleaned_df"].convert_dtypes().infer_objects()

# 🔐 Load API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@st.cache_data(show_spinner=True)
def generate_gpt_insight(data: pd.DataFrame) -> str:
    # Use smaller sample to save tokens
    sample_df = data.sample(min(len(data), 50), random_state=42)

    summary = sample_df.describe(include='all').to_string()
    numeric_df = sample_df.select_dtypes(include='number')

    correlation = (
        numeric_df.corr().to_string()
        if not numeric_df.empty
        else "No numeric columns to compute correlation."
    )

    prompt = f"""
You are a senior data analyst. Analyze the following dataset sample
based on its summary statistics and correlation table.
Find 3–5 key insights that would help a business make decisions.

### Summary Stats:
{summary}

### Correlation Matrix:
{correlation}

Return your response in bullet points, using simple and professional language.
"""

    # Retry logic for rate limits
    for attempt in range(3):
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful data science assistant."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.4,
                max_tokens=300
            )
            return response.choices[0].message.content
        except RateLimitError:
            wait_time = (2 ** attempt) * 2  # exponential backoff
            time.sleep(wait_time)

    return "⚠️ API rate limit reached multiple times. Please try again later."

# Only run on button click
if st.button("🔍 Generate Insights with AI"):
    with st.spinner("Analyzing data using GPT..."):
        insights = generate_gpt_insight(df)
        st.subheader("💡 Key Insights:")
        st.markdown(insights)
