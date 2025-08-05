# 5 Strategy Module
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from prophet import Prophet
import plotly.express as px
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, mean_squared_error, r2_score

st.set_page_config(layout="wide")
st.title("📊 Strategy Builder: ML Models")

if "cleaned_df" not in st.session_state:
    st.warning("⚠️ No cleaned data found. Please upload and clean your dataset first.")
    st.stop()

df = st.session_state["cleaned_df"]

tab1, tab2, tab3 = st.tabs(["📍 Clustering", "📅 Forecasting", "📊 ML Models"])

# ------------ TAB 1: KMeans Clustering ------------
with tab1:
    st.subheader("🧩 KMeans Clustering")

    num_cols = df.select_dtypes(include=["int64", "float64"]).columns.tolist()

    if len(num_cols) < 2:
        st.error("❌ Need at least 2 numerical columns for clustering.")
    else:
        x_col = st.selectbox("X-axis Feature", num_cols)
        y_col = st.selectbox("Y-axis Feature", [col for col in num_cols if col != x_col])
        n_clusters = st.slider("Number of Clusters", 2, 10, 3)

        kmeans = KMeans(n_clusters=n_clusters, random_state=0)
        df_cluster = df[[x_col, y_col]].dropna().copy()
        df_cluster["Cluster"] = kmeans.fit_predict(df_cluster[[x_col, y_col]])

        fig = px.scatter(df_cluster, x=x_col, y=y_col, color=df_cluster["Cluster"].astype(str),
                         title=f"KMeans Clustering ({x_col} vs {y_col})")
        st.plotly_chart(fig, use_container_width=True)

# ------------ TAB 2: Time Series Forecasting ------------
with tab2:
    st.subheader("📈 Prophet Time Series Forecast")

    date_col = st.selectbox("Select date column", df.columns)
    metric_col = st.selectbox("Select value to forecast", df.select_dtypes(include=["int64", "float64"]).columns)

    if st.button("Forecast"):
        try:
            df_prophet = df[[date_col, metric_col]].dropna().copy()
            df_prophet[date_col] = pd.to_datetime(df_prophet[date_col])
            df_prophet = df_prophet.rename(columns={date_col: "ds", metric_col: "y"})

            model = Prophet()
            model.fit(df_prophet)

            future = model.make_future_dataframe(periods=30)
            forecast = model.predict(future)

            fig = px.line(forecast, x='ds', y='yhat', title='📈 Forecasted Values (30 days ahead)')
            st.plotly_chart(fig, use_container_width=True)

        except Exception as e:
            st.error(f"❌ Forecast failed: {e}")

# ------------ TAB 3: Machine Learning Models ------------
with tab3:
    st.subheader("🧪 Run a Machine Learning Model")

    task = st.selectbox("Select Task Type", ["Classification", "Regression"])

    target_col = st.selectbox("🎯 Select Target Column", df.columns)
    feature_cols = st.multiselect("🧠 Select Feature Columns (inputs)", [col for col in df.columns if col != target_col])

    if st.button("🚀 Train Model"):
        try:
            X = df[feature_cols]
            y = df[target_col]

            # Encode categorical variables
            X = pd.get_dummies(X, drop_first=True)

            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

            if task == "Classification":
                model = RandomForestClassifier()
                model.fit(X_train, y_train)
                preds = model.predict(X_test)
                acc = accuracy_score(y_test, preds)
                st.success(f"✅ Classification Accuracy: **{acc:.2f}**")

            elif task == "Regression":
                model = LinearRegression()
                model.fit(X_train, y_train)
                preds = model.predict(X_test)
                mse = mean_squared_error(y_test, preds)
                r2 = r2_score(y_test, preds)
                st.success(f"📉 Regression MSE: **{mse:.2f}** | R² Score: **{r2:.2f}**")

        except Exception as e:
            st.error(f"⚠️ Model training failed: {e}")
