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
st.subheader("Top 10 Countries")

fig, ax = plt.subplots()

df["country"].value_counts().head(10).plot(kind="bar", ax=ax)

st.pyplot(fig)
st.subheader("Top 10 Ratings")

fig, ax = plt.subplots()

df["rating"].value_counts().head(10).plot(kind="bar", ax=ax)

st.pyplot(fig)
st.subheader("Content Released by Year")

fig, ax = plt.subplots()

df["release_year"].value_counts().sort_index().plot(kind="line", ax=ax)

st.pyplot(fig)
st.subheader("Top 10 Genres")

fig, ax = plt.subplots()

df["listed_in"].value_counts().head(10).plot(kind="bar", ax=ax)

st.pyplot(fig)
st.subheader("Top 10 Durations")

fig, ax = plt.subplots()

df["duration"].value_counts().head(10).plot(kind="bar", ax=ax)

st.pyplot(fig)
st.subheader("Content Added to Netflix by Year")

df["date_added"] = pd.to_datetime(df["date_added"], errors="coerce")
df["Year Added"] = df["date_added"].dt.year

fig, ax = plt.subplots()

df["Year Added"].value_counts().sort_index().plot(kind="line", ax=ax)

st.pyplot(fig)
