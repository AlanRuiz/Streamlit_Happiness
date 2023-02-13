import streamlit as st
import plotly.express as px
import pandas as pd

df = pd.read_csv("happy.csv")
gdp = df['gdp'].to_list()
happiness = df['happiness'].to_list()
generosity = df["generosity"].tolist()


st.title("In search for Happiness")
x_axis_selection = st.selectbox("Select the data for the X-Axis",("GDP","Happiness","Generosity"))
y_axis_selection = st.selectbox("Select the data for the Y-Axis",("GDP","Happiness","Generosity"))
st.title(f"{x_axis_selection} & {y_axis_selection}")

match x_axis_selection:
    case "GDP":
        x_selection = df['gdp'].to_list()
    case "Happiness":
        x_selection = df['happiness'].to_list()
    case "Generosity":
        x_selection = df['happiness'].to_list()

match y_axis_selection:
    case "GDP":
        y_selection = df['gdp'].to_list()
    case "Happiness":
        y_selection = df['happiness'].to_list()
    case "Generosity":
        y_selection = df['happiness'].to_list()


figure = px.scatter(x=x_selection, y=y_selection, labels={"x":f"{x_axis_selection}", "y":f"{y_axis_selection}"})

st.plotly_chart(figure)
