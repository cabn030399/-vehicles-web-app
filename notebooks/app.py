import pandas as pd
import plotly.express as px
import streamlit as st

# Configurar la página
st.title('Análisis de la Premier League 2025')
st.header('Exploración de datos de partidos de fútbol')

# Cargar los datos
@st.cache_data
def load_data():
    return pd.read_csv('premier_league_2025.csv')

# Cargar el dataset
premier_data = load_data()

# Mostrar información básica
st.subheader('Información del dataset')
st.write(f'Total de partidos: {len(premier_data)}')
st.write(f'Partidos con resultado: {premier_data["Result"].notna().sum()}')
st.write(f'Partidos pendientes: {premier_data["Result"].isna().sum()}')