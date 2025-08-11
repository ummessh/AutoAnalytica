import streamlit as st
import pandas as pd
import os
from openai import OpenAI

st.title("💬 Data Chatbot")

if "cleaned_df" not in st.session_state:
    st.warning("⚠️ No cleaned data found. Please upload and clean a dataset first.")
    st.stop()

df = st.session_state["cleaned_df"]
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def chat_with_data(question, data):
    preview = data.head(20).to_csv(index=False)
    prompt = f"""
You are a helpful data analyst. You can only answer based on the dataset provided.
Dataset preview:
{preview}

User question:
{question}

If you need to calculate something, explain your reasoning step-by-step.
"""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an expert data analyst."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )
    return response.choices[0].message.content

user_question = st.text_input("Ask me anything about your dataset:")
if st.button("Ask"):
    with st.spinner("Thinking..."):
        answer = chat_with_data(user_question, df)
        st.markdown(answer)
