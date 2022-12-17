import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np


url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQyG--czZ6babMu7IIUyv_lDHNNIMbOT5orCJafwvahFmtrqJoIjbhG3JcINpCL4Kvz4U-lP-_fZg1a/pub?output=csv'
#Title
st.markdown("<h1 style='text-align: center; color: White;'>Porcentaje de grupos de edad para los colombianos en el exterior </h1>", unsafe_allow_html=True)
#Loading data

@st.cache
def cargar_datos(filename: str):
    return pd.read_csv(filename,sep=";")

datos = cargar_datos(url)

#body



#graphics
#@st.cache(allow_output_mutation=True)
def graph_pie(df):
    fig = px.pie(df.groupby(["EDAD", "GRUPO EDAD"]).count().reset_index(),
        values="EDAD",
        names="GRUPO EDAD",
        color_discrete_sequence=px.colors.qualitative.Set3,    
    )
    fig.update_traces(textposition='inside', textinfo='percent+label')
    return fig

st.plotly_chart(
    graph_pie(datos),
    use_container_width=True,
)

