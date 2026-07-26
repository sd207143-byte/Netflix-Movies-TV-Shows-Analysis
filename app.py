import streamlit as st
import pandas as pd

st.title("🎬 Netflix Movies & TV Shows Analysis")

df = pd.read_csv("netflix_titles.csv")

st.subheader("Netflix Dataset")

st.dataframe(df)
