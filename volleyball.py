import streamlit as st
import pandas as pd
import altair as alt

volleyball_df = pd.read_csv('WSSU Volleyball Data.csv')

source = volleyball_df

alt.Chart(source).mark_bar().encode(
    x='Player',
    y='Kills'
)

