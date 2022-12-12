import streamlit as st
import pandas as pd
import numpy as np
import datetime
from datetime import date
import openpyxl

st.title("Jogos do Dia")

dia = st.date_input(
    "Data de Análise",
    date.today())

def load_data_jogos():
    data_jogos = pd.read_excel("https://github.com/rpthiago/JogosHoje/blob/main/lay_away.xlsx?raw=true")
    
    return data_jogos

df_jogos = load_data_jogos()

st.dataframe(df_jogos)
