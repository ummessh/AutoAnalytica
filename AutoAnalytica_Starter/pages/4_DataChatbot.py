import streamlit as st
import pandas as pd
import os
from openai import OpenAI

st.title("💬 Data Chatbot — Ask About Your Data")

if "cleaned_df" not in st.session_state:
    st.warning("⚠️ No cleaned data found. Please upload and clean a dataset first.")
    st.stop()

df = st.session_state["cleaned_df"]
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Example questions to guide the user
example_questions = [
    "What are the top 5 highest values in the dataset?",
    "Which column has the most missing values?",
    "Give me a summary of the dataset in simple words.",
    "What trends do you see in the data?",
    "Are there any outliers in the numeric columns?"
]

def chat_with_data(question, data):
    preview = data.head(20).to_csv(index=False)
    prompt = f"""
You are a friendly and helpful data analyst. Use only the dataset provided.
Dataset preview:
{preview}

User question:
{question}

If calculations are needed, explain them clearly but keep the tone supportive and simple.
"""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a supportive and expert data analyst."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
        max_tokens=400
    )
    return response.choices[0].message.content

# Let the user pick an example or type their own
st.markdown("💡 **Need ideas?** Choose an example below or type your own question.")
chosen_example = st.selectbox("Pick an example question:", [""] + example_questions)
custom_question = st.text_input("Or type your own question:")

final_question = custom_question if custom_question.strip() else chosen_example

if st.button("Ask"):
    if not final_question.strip():
        st.warning("Please type a question or choose an example first.")
    else:
        with st.spinner("Thinking..."):
            answer = chat_with_data(final_question, df)
            st.markdown("### 💡 Answer:")
            st.markdown(answer)
