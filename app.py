import pandas as pd
import plotly.express as px
import streamlit as st

# Page configuration
st.set_page_config(page_title="Premier Fantasy Football League", layout="wide")

st.title("📊 League Statistics")

# Load sample or custom data
df = px.data.iris()

# Sidebar filters
st.sidebar.header("League Chooser")
species = st.sidebar.multiselect(
    "Select Species", df["species"].unique(), default=df["species"].unique()
)

# Filter dataframe
filtered_df = df[df["species"].isin(species)]

# Display metrics and data
st.metric("Total Records", len(filtered_df))
st.dataframe(filtered_df)

# Plot chart
fig = px.scatter(
    filtered_df, x="sepal_width", y="sepal_length", color="species"
)
st.plotly_chart(fig, use_container_width=True)
