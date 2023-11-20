import streamlit as st
import pandas as pd
import altair as alt

volleyball_df = pd.read_csv('WSSU Volleyball Data.csv')
st.dataframe(volleyball_df)

source = volleyball_df

alt.Chart(source).mark_bar().encode(
    x='Player',
    y='Kills'
)

