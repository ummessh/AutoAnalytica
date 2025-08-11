import streamlit as st
import pandas as pd
import os
import time
from openai import OpenAI, RateLimitError, APIError

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
            st.warning(f"⚠️ API rate limit hit. Retrying in {wait_time} seconds...")
            time.sleep(wait_time)
        except APIError as e:
            if "insufficient_quota" in str(e):
                return "❌ Your OpenAI quota has been exceeded. Please check your plan or billing details."
            else:
                return f"⚠️ API Error: {e}"

    return "⚠️ API rate limit reached multiple times. Please try again later."

# Example question suggestions
example_questions = [
    "Which columns have the strongest correlation?",
    "Are there any surprising trends in the data?",
    "Which factors seem most related to the target variable?",
    "What patterns stand out in the numerical data?",
    "Are there any anomalies or unusual values?"
]

with st.expander("💡 Example Questions to Ask the AI"):
    st.write("Here are some ideas to get you started:")
    for q in example_questions:
        st.markdown(f"- {q}")

# Only run on button click
if st.button("🔍 Generate Insights with AI"):
    with st.spinner("Analyzing data using GPT..."):
        insights = generate_gpt_insight(df)
        st.subheader("💡 Key Insights:")
        st.markdown(insights)
