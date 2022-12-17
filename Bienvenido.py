import streamlit as st
import pandas as pd
import plotly.express as px

url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vRmR6eCVm8JAhFLi53wF0-y-R9CpbzcnwJBWhliPrYrzi6td1XEZuDWqUSklCLqPGenlUzSAm837ZKb/pub?output=csv'
st.set_page_config(layout="wide")
st.header("App para el Diplomado de Python")
APP_TITLE = 'Colombianos en el Extranjero'

@st.cache
def cargar_datos(filename: str):
    return pd.read_csv(filename,sep=";")

datos = cargar_datos(url)

st.markdown("<h1 style='text-align: center; color: White;'>BIENVENIDOS </h1>", unsafe_allow_html=True)
st.markdown("---")

st.markdown("Bienvenidos al tablero digital del Grupo , en este tablero se mostraran datos los cuales creemos que son relevantes para la toma de desiciones. Los datos utilizados para este análisis tiene por nombre Colombianos Registrados en el Extranjero, dicho dataset se encuentra información sociodemografica de los colombianos que se encuentran en el extranjero.")

st.markdown("---")

st.markdown("Número de Colombianos en el extranjero.")
#st.markdown('{:,}'.format(datos['CANTIDAD DE PERSONAS'].sum()))
