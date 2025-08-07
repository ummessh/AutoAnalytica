# 2 AutoEDA
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import missingno as msno
import plotly.express as px
from numpy import nan

st.title("📊 Auto Exploratory Data Analysis (EDA)")

# Session check
if 'uploaded_df' not in st.session_state:
    st.warning("⚠️ No file uploaded. Please go to 'Upload Data' and upload a CSV.")
    st.stop()

# Load data from session
df = st.session_state['uploaded_df']
st.success(f"Using uploaded file: {st.session_state.get('uploaded_filename', 'Unnamed')}")
st.dataframe(df.head(), use_container_width=True)

# -----------------------------------
# 🧼 CLEANING invalid values as NaN
invalid_map = {
    "Age": [177],
    "Cabin": [687],
    "Embarked": [2]
}
for col, invalids in invalid_map.items():
    if col in df.columns:
        df[col] = df[col].replace(invalids, nan)

def sanitize_dataframe(df):
    for col in df.columns:
        if df[col].dtype == 'object':
            df[col] = df[col].astype(str)  # Force all objects to string
        elif df[col].apply(lambda x: isinstance(x, (list, dict, set, tuple))).any():
            df[col] = df[col].apply(str)  # Handle mixed or complex types
    return df

# Store cleaned version back (optional)
df = sanitize_dataframe(df)
st.session_state['cleaned_df'] = df  # Store for Insights AI or DataChatbot

# Section 1: Basic Info
st.subheader("📌 Dataset Overview")
st.write(f"**Shape:** {df.shape[0]} rows × {df.shape[1]} columns")
st.write("**Column data types:**")
st.dataframe(df.dtypes.astype(str).reset_index().rename(columns={'index': 'Column', 0: 'Type'}), use_container_width=True)

# Section 2: Null Matrix with summary
st.subheader("🧼 Missing Value Matrix")

missing_total = df.isna().sum().sum()
if missing_total == 0:
    st.info("✅ No missing or invalid values detected.")
else:
    st.warning(f"❗ Missing values detected in {df.isna().any().sum()} columns (Total missing cells: {missing_total})")

with st.container():
    fig, ax = plt.subplots()
    msno.matrix(df, ax=ax, sparkline=False)
    st.pyplot(fig)

# Section 3: Summary Stats
st.subheader("📋 Summary Statistics")
st.dataframe(df.describe(include='all'), use_container_width=True)

# Section 4: Feature Distribution
st.subheader("📈 Feature Distribution")
num_cols = df.select_dtypes(include=["float64", "int64"]).columns.tolist()

if num_cols:
    selected_dist_col = st.selectbox("Select a numeric column", num_cols)
    if selected_dist_col:
        with st.container():
            fig = px.histogram(df, x=selected_dist_col, nbins=30, title=f'Distribution of {selected_dist_col}')
            fig.update_layout(
                plot_bgcolor='rgba(240,240,240,0.95)',
                paper_bgcolor='white',
                margin=dict(l=40, r=40, t=40, b=40),
                font=dict(size=14)
            )
            st.plotly_chart(fig, use_container_width=True)
else:
    st.info("No numeric columns available for distribution plot.")

# Section 5: Correlation Heatmap
if len(num_cols) >= 2:
    st.subheader("🔍 Correlation Heatmap")
    corr = df[num_cols].corr()
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f", ax=ax)
    st.pyplot(fig)
else:
    st.info("Not enough numeric columns for correlation heatmap.")
