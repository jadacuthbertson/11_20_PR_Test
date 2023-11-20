import streamlit as st
import pandas as pd

volleyball_df = pd.read_csv('WSSU Volleyball Data.csv')

st.dataframe(volleyball_df)