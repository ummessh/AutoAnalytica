import streamlit as st
import pandas as pd

st.title("Upload Data")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    st.markdown(f"### 📄 **{uploaded_file.name}**")
    st.markdown("#### 🔍 Preview of Uploaded Data")
    st.dataframe(df.head())

    # 🧼 Data Cleaning Summary
    st.markdown("### 🧼 Data Cleaning Summary")
    missing_values = df.isnull().sum()
    missing_dict = missing_values[missing_values > 0].to_dict()
    
    if len(missing_dict) == 0:
        st.info("✅ No missing values found in the dataset.")
    else:
        st.json(missing_dict)

    # 🔧 Cleaning Options
    st.markdown("### ⚙️ Apply Cleaning Options")
    drop_nulls = st.checkbox("Drop rows with any nulls?")
    
    if drop_nulls:
        df = df.dropna()
        st.success("✅ Null rows dropped.")
    
    fill_null_value = st.selectbox("Or fill null values with:", ["None", "0", "Mean", "Median"])
    
    if fill_null_value != "None":
        for col in df.select_dtypes(include='number').columns:
            if df[col].isnull().sum() > 0:
                if fill_null_value == "0":
                    df[col] = df[col].fillna(0)
                elif fill_null_value == "Mean":
                    df[col] = df[col].fillna(df[col].mean())
                elif fill_null_value == "Median":
                    df[col] = df[col].fillna(df[col].median())
        st.success(f"✅ Nulls filled with {fill_null_value.lower()}.")

    st.markdown("#### ✅ Final Cleaned Data Preview")
    st.dataframe(df.head())

