 
import streamlit as st
import pandas as pd
import plotly.express as px

# Configuración de la página
st.set_page_config(page_title="Análisis Premier League 2025", layout="wide")

# Título principal
st.title("Análisis de la Premier League 2025")

# Cargar datos
@st.cache_data
def load_data():
    return pd.read_csv('premier_league_2025.csv')

premier_data = load_data()

# Información básica del dataset
st.subheader('Información del Dataset')
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total de partidos", len(premier_data))

with col2:
    partidos_con_resultado = premier_data['Result'].notna().sum()
    st.metric("Partidos con resultado", partidos_con_resultado)

with col3:
    partidos_pendientes = premier_data['Result'].isna().sum()
    st.metric("Partidos pendientes", partidos_pendientes)