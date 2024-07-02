# This is a template for a streamlit live task.
# This generates an app with one dataframe as input. Then the user can select 2 columns to plot a scatter plot.

from typing import List

import streamlit as st
from gws_core import Resource
from pandas import DataFrame
from plot.plot_generator import generate_scatter_plot

# thoses variable will be set by the streamlit app
# don't initialize them, there are create to avoid errors in the IDE
sources: List[Resource]
params: dict

# Your Streamlit app code here
st.title(params.get('title'))

# show a table from file_path which is a csv file full width
if sources:
    df: DataFrame = sources[0].get_data()

    # show the dataframe
    st.dataframe(df)

    # add a select widget with the columns names with no default value
    # set the selectbox side by side
    col1, col2 = st.columns(2)

    with col1:
        x_col = st.selectbox("Select x column", options=df.columns, index=0)

    with col2:
        y_col = st.selectbox("Select y column", options=df.columns, index=1)

    generate_scatter_plot(df, x_col, y_col)
