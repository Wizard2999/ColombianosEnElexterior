import streamlit as st
import requests
import pandas as pd
import plotly.express as px
import numpy as np



#Title
st.markdown("<h1 style='text-align: center; color: White;'>Gráficos de Barras </h1>", unsafe_allow_html=True)
#Loading data
url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vRmR6eCVm8JAhFLi53wF0-y-R9CpbzcnwJBWhliPrYrzi6td1XEZuDWqUSklCLqPGenlUzSAm837ZKb/pub?output=csv'
@st.cache
def cargar_datos(filename: str):
    return pd.read_csv(filename,sep=";")


datos = cargar_datos(url)

st.markdown("# Cantidad de personas por área de conocimiento de los colombianos en el exterior")

@st.cache(allow_output_mutation=True)
def graph_bar3(df):
    fig =  px.bar(
        df.groupby(["AREA_CONOCIMIENTO"])["CANTIDAD DE PERSONAS"]
        .count(),
        y ="CANTIDAD DE PERSONAS",
        log_y=True)
    return fig

st.plotly_chart(
   graph_bar3(datos),
    use_container_width=False, 
)


st.markdown("# Nivel academico de colombianos en el exterior")

#@st.cache(allow_output_mutation=True)
def graph_bar2(df):
    fig = px.bar(
        df.groupby(["NIVEL_ACADEMICO"])["CANTIDAD DE PERSONAS"]
        .count(),
        y ="CANTIDAD DE PERSONAS",
        log_y=True
    )
    return fig

st.plotly_chart(
    graph_bar2(datos),
    use_container_width=False, 
)