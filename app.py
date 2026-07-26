import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("🎬 Netflix Movies & TV Shows Analysis")

df = pd.read_csv("netflix_titles.csv")

st.subheader("Netflix Dataset")

st.dataframe(df)

st.subheader("Movies vs TV Shows")

fig, ax = plt.subplots()

df["type"].value_counts().plot(kind="bar", ax=ax)

st.pyplot(fig)
