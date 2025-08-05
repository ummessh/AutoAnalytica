import streamlit as st
import pandas as pd
from utils.cleaning import generate_cleaning_report, apply_cleaning_options

st.title("📤 Upload & Clean Your Dataset")

# Upload CSV or Excel
uploaded_file = st.file_uploader("Upload your CSV or Excel file", type=["csv", "xlsx"])

if uploaded_file:
    try:
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)
        
        st.subheader("🔍 Preview of Uploaded Data")
        st.dataframe(df.head())

        # Cleaning Summary
        st.subheader("🧼 Data Cleaning Summary")
        report = generate_cleaning_report(df)
        st.json(report, expanded=False)

        # Cleaning Options
        st.subheader("⚙️ Apply Cleaning Options")
        drop_nulls = st.checkbox("Drop rows with any nulls?")
        fill_nulls = st.selectbox("Fill null values with:", ["None", "Mean", "Median", "Mode"])
        drop_duplicates = st.checkbox("Drop duplicate rows?")
        drop_constant = st.checkbox("Drop constant columns?")

        if st.button("Apply Cleaning"):
            df_cleaned = apply_cleaning_options(df, drop_nulls, fill_nulls, drop_duplicates, drop_constant)
            st.success("✅ Cleaning Applied!")
            st.dataframe(df_cleaned.head())

            # Optionally save cleaned dataframe to session for next page
            st.session_state["cleaned_df"] = df_cleaned

    except Exception as e:
        st.error(f"❌ Error loading file: {e}")
