import streamlit as st
import pandas as pd

st.title("📂 Upload Data")

# Initialize session variables if not present
if "uploaded_df" not in st.session_state:
    st.session_state["uploaded_df"] = None
if "uploaded_filename" not in st.session_state:
    st.session_state["uploaded_filename"] = None

# File uploader – only reset if no file already stored
uploaded_file = st.file_uploader(
    "Upload a CSV file",
    type=["csv"],
    key="file_uploader"
)

# If new file uploaded, replace stored dataframe
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.session_state["uploaded_df"] = df
    st.session_state["uploaded_filename"] = uploaded_file.name

# If a file was uploaded before, use it
if st.session_state["uploaded_df"] is not None:
    df = st.session_state["uploaded_df"]

    st.success(f"✅ Using file: `{st.session_state['uploaded_filename']}`")
    st.dataframe(df)

    # 🧼 Data Cleaning Summary
    st.markdown("### 🧼 Data Cleaning Summary")
    missing_values = df.isnull().sum()
    missing_dict = missing_values[missing_values > 0].to_dict()

    if len(missing_dict) == 0:
        st.info("✅ No missing values found in the dataset.")
    else:
        st.markdown("#### 🔎 Null values in each column:")
        for col, count in missing_dict.items():
            st.markdown(f"- **{col}**: {count} null values")

    # 🔧 Cleaning Options
    st.markdown("### ⚙️ Apply Cleaning Options")
    drop_nulls = st.checkbox("Drop rows with any nulls?")

    if drop_nulls:
        df = df.dropna()
        st.session_state["uploaded_df"] = df
        st.success("✅ Null rows dropped.")

    fill_null_value = st.selectbox("Or fill null values with:", ["None", "0", "Mean", "Median"])

    if fill_null_value != "None":
        for col in df.select_dtypes(include="number").columns:
            if df[col].isnull().sum() > 0:
                if fill_null_value == "0":
                    df[col] = df[col].fillna(0)
                elif fill_null_value == "Mean":
                    df[col] = df[col].fillna(df[col].mean())
                elif fill_null_value == "Median":
                    df[col] = df[col].fillna(df[col].median())
        st.session_state["uploaded_df"] = df
        st.success(f"✅ Nulls filled with {fill_null_value.lower()}.")

    st.markdown("#### ✅ Final Cleaned Data Preview")
    st.dataframe(df)
else:
    st.warning("⚠️ No file uploaded yet.")
