import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

#Title
st.markdown("<h1 style='text-align: center; color: White;'>Mapa Interactivo. </h1>", unsafe_allow_html=True)
st.markdown("Revision de colombianos por todo el mapa")
url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vRmR6eCVm8JAhFLi53wF0-y-R9CpbzcnwJBWhliPrYrzi6td1XEZuDWqUSklCLqPGenlUzSAm837ZKb/pub?output=csv'

#Loading data
@st.cache(allow_output_mutation=True)
def cargar_datos1(filename: str):
    return pd.read_csv(filename,sep=";")

datos = cargar_datos1(url)

pais = st.selectbox(label="Busqueda por pais", options=datos["PAIS"].unique())
@st.cache(allow_output_mutation=True)
def grap(df,ps):
    df = df.dropna()
    df = df[df["PAIS"]==ps]
    fig = px.scatter_mapbox(df,
                        lat=df.LocalizaciónY,
                        lon=df.LocalizaciónX,
                        size="CANTIDAD DE PERSONAS",
                        zoom=6,
                        hover_data=["CANTIDAD DE PERSONAS"],
                        hover_name="PAIS",
                        color_discrete_sequence=["fuchsia"],
                        #center = {'lat': 8.74798, 'lon': -75.88143},
                        #size_max=15,
                        #height=300
                        #projection="natural earth"
                        )
    fig.update_layout(mapbox_style="open-street-map")
    #fig.update_traces(cluster=dict(enabled=True))
    #fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    return fig

st.plotly_chart(
    grap(datos,pais),
    use_container_width=True,
)
