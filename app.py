import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("📊 EDA Dashboard")

# FIXED: correct loading
df = pd.read_csv("Housing1.csv")

# Preview
st.subheader("Dataset Preview")
st.write(df.head())

# Info
st.subheader("Dataset Info")
st.write(df.describe())

# Select column
st.subheader("Select Column for Analysis")
col = st.selectbox("Choose column", df.columns)

# Histogram
st.subheader("Histogram")
fig, ax = plt.subplots()
sns.histplot(df[col], kde=True, ax=ax)
st.pyplot(fig)

# Boxplot
st.subheader("Boxplot")
fig2, ax2 = plt.subplots()
sns.boxplot(x=df[col], ax=ax2)
st.pyplot(fig2)