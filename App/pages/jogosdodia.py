import streamlit as st
import pandas as pd
import numpy as np
import datetime
from datetime import date

st.title("Jogos do Dia")

def load_data_jogos():
    data_jogos = pd.read_xlsx("https://github.com/rpthiago/JogosHoje/blob/main/jogos_dia_completo.xlsx?raw=true")
    
    return data_jogos

df_jogos = load_data_jogos()

st.dataframe(df_jogos)
