# ============================================================
# Healthcare Costs EDA Dashboard - Streamlit Version
# ============================================================

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(page_title="Healthcare EDA", layout="wide")

st.title("🏥 Healthcare Costs & Demographics Dashboard")
st.markdown("Interactive EDA powered by Streamlit + Plotly")

# =========================
# LOAD DATA
# =========================
df = pd.read_csv("insurance.csv")

# =========================
# SIDEBAR FILTERS
# =========================
st.sidebar.header("🔍 Filters")

sex_filter = st.sidebar.multiselect("Gender", df["sex"].unique(), default=df["sex"].unique())
smoker_filter = st.sidebar.multiselect("Smoker", df["smoker"].unique(), default=df["smoker"].unique())
region_filter = st.sidebar.multiselect("Region", df["region"].unique(), default=df["region"].unique())

filtered_df = df[
    (df["sex"].isin(sex_filter)) &
    (df["smoker"].isin(smoker_filter)) &
    (df["region"].isin(region_filter))
]

# =========================
# TABS
# =========================
tab1, tab2, tab3, tab4 = st.tabs([
    "📊 Overview",
    "📈 Distributions",
    "🔗 Relationships",
    "🔥 Insights"
])

# ============================================================
# TAB 1 - OVERVIEW
# ============================================================
with tab1:
    st.subheader("Dataset Overview")

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Records", len(filtered_df))
    col2.metric("Average Expenses", round(filtered_df["expenses"].mean(), 2))
    col3.metric("Average BMI", round(filtered_df["bmi"].mean(), 2))

    st.dataframe(filtered_df)

    st.subheader("Missing Values")
    st.write(filtered_df.isnull().sum())

# ============================================================
# TAB 2 - DISTRIBUTIONS
# ============================================================
with tab2:
    st.subheader("Distributions")

    col1, col2 = st.columns(2)

    with col1:
        fig = px.histogram(filtered_df, x="age", nbins=20, title="Age Distribution")
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        fig = px.histogram(filtered_df, x="bmi", nbins=20, title="BMI Distribution")
        st.plotly_chart(fig, use_container_width=True)

    fig = px.histogram(filtered_df, x="expenses", nbins=30, title="Medical Expenses Distribution")
    st.plotly_chart(fig, use_container_width=True)

    col3, col4 = st.columns(2)

    with col3:
        fig = px.bar(filtered_df["sex"].value_counts(), title="Gender Distribution")
        st.plotly_chart(fig, use_container_width=True)

    with col4:
        fig = px.bar(filtered_df["smoker"].value_counts(), title="Smoking Status")
        st.plotly_chart(fig, use_container_width=True)

# ============================================================
# TAB 3 - RELATIONSHIPS
# ============================================================
with tab3:
    st.subheader("Relationships")

    fig = px.scatter(
        filtered_df,
        x="age",
        y="expenses",
        color="smoker",
        title="Age vs Expenses"
    )
    st.plotly_chart(fig, use_container_width=True)

    fig = px.scatter(
        filtered_df,
        x="bmi",
        y="expenses",
        color="smoker",
        title="BMI vs Expenses"
    )
    st.plotly_chart(fig, use_container_width=True)

    fig = px.box(filtered_df, x="smoker", y="expenses", title="Expenses by Smoking Status")
    st.plotly_chart(fig, use_container_width=True)

    fig = px.box(filtered_df, x="sex", y="expenses", title="Expenses by Gender")
    st.plotly_chart(fig, use_container_width=True)

    fig = px.box(filtered_df, x="region", y="expenses", title="Expenses by Region")
    st.plotly_chart(fig, use_container_width=True)

# ============================================================
# TAB 4 - INSIGHTS
# ============================================================
with tab4:
    st.subheader("Key Insights (Auto Summary)")

    st.markdown("""
    ### 🧠 What the data reveals:

    - 🔥 Smokers have significantly higher medical expenses  
    - 📈 Age increases strongly affect healthcare cost  
    - ⚖️ BMI is positively correlated with expenses  
    - 👤 Gender has minimal impact  
    - 🌍 Regional differences exist but are small  
    """)

    st.subheader("Correlation Heatmap")

    corr = filtered_df.select_dtypes(include=np.number).corr()
    fig = px.imshow(corr, text_auto=True, color_continuous_scale="RdBu_r")
    st.plotly_chart(fig, use_container_width=True)

# =========================
# FOOTER
# =========================
st.markdown("---")
st.success("✅ EDA Dashboard Loaded Successfully")