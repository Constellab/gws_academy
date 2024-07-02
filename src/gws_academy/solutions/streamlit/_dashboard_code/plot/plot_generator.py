
import plotly.express as px
import streamlit as st
from pandas import DataFrame


def generate_scatter_plot(dataframe: DataFrame, x_col: str, y_col: str) -> None:
    if x_col and y_col:
        # Generate a scatter plot with plotly express
        fig = px.scatter(dataframe, x=x_col, y=y_col)
        st.plotly_chart(fig)
