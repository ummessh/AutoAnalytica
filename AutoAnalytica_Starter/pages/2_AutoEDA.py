# 2 AutoEDA
# 2 AutoEDA
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import missingno as msno
import plotly.express as px
from io import BytesIO

st.title("📊 Auto Exploratory Data Analysis (EDA)")

# Check if data exists
if "cleaned_df" not in st.session_state:
    st.warning("⚠️ No cleaned data found. Please upload and clean a dataset first.")
    st.stop()

df = st.session_state["cleaned_df"]

# Section 1: Basic Info
st.subheader("📌 Dataset Overview")
st.write("Shape of dataset:", df.shape)
st.write("Column data types:")
st.write(df.dtypes)

# Section 2: Null Matrix
st.subheader("🧼 Missing Value Matrix")
fig, ax = plt.subplots()
msno.matrix(df, ax=ax)
st.pyplot(fig)

# Section 3: Summary Stats
st.subheader("📋 Summary Statistics")
st.dataframe(df.describe(include='all'), use_container_width=True)

# Section 4: Distribution Plot
st.subheader("📈 Feature Distribution")
num_cols = df.select_dtypes(include=["float64", "int64"]).columns.tolist()
selected_dist_col = st.selectbox("Select a numeric column", num_cols)

if selected_dist_col:
    fig = px.histogram(df, x=selected_dist_col, nbins=30, title=f'Distribution of {selected_dist_col}')
    st.plotly_chart(fig, use_container_width=True)

# Section 5: Correlation Heatmap
if len(num_cols) >= 2:
    st.subheader("🔍 Correlation Heatmap")
    corr = df[num_cols].corr()
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f", ax=ax)
    st.pyplot(fig)
