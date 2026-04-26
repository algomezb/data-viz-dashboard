import pandas as pd
import plotly.express as px
import streamlit as st

st.title("Irish Evolution housing prices and labor force")

df = pd.read_csv("./csv/prices-counties-2025.csv")
print(df.head())
county_avg = df.groupby("county")["price"].transform("mean")
df_sorted = (
    df.assign(county_avg=county_avg)
    .sort_values("county_avg", ascending=False)
    .drop(columns="county_avg")
)
fig = px.box(
    df_sorted,
    x="county",
    y="price",
    color="county",
    template="plotly_white",
    points=False,
    labels={"price": "Price", "county": "County"},
)

st.plotly_chart(fig)


agg = pd.read_csv("./csv/number-sales-county-year.csv")
fig = px.bar(
    agg,
    x="year",
    y="count",
    color="county",
    template="plotly_white",
    labels={"year": "Year", "count": "Number of Sales", "county": "County"},
)
st.plotly_chart(fig)
