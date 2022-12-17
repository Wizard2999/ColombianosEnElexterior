import streamlit as st
import requests
import pandas as pd
import plotly.express as px

url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQyG--czZ6babMu7IIUyv_lDHNNIMbOT5orCJafwvahFmtrqJoIjbhG3JcINpCL4Kvz4U-lP-_fZg1a/pub?output=csv'
st.markdown("<h1 style='text-align: center; color: White;'>Predicción </h1>", unsafe_allow_html=True)


def cargar_datos(filename: str):
    return pd.read_csv(filename,sep=";")

datos = cargar_datos(url)

st.markdown('En base a que aparecen en la parte de abajo se puede predecir el país al que nos puede ir mejor si decidimos salir al extranjero')

AREA_CONOCIMIENTO_1 = st.selectbox(label="Área de Conocimiento",
                                 options=['ECONOMIA ADMINISTRACION CONTADURIA Y AFINES', 'NINGUNA',
        'CIENCIAS DE LA EDUCACION', 'BELLAS ARTES', 'NO INDICA',
        'INGENIERÍA, ARQUITECTURA Y AFINES', 'CIENCIAS SOCIALES Y HUMANAS',
        'CIENCIAS DE LA SALUD', 'AGRONOMÍA, VETERINARIA Y AFINES',
        'MATEMATICAS Y CIENCIAS NATURALES', 'NO REGISTRA',
        'COCINA Y CULINARIA', 'AGRONOMIA VETERINARIA Y ZOOTECNIA',
        'AVIACION'])
ESTADO_CIVIL_2 = st.selectbox(label="Estado Civil",
                            options=['CASADO', 'UNION_LIBRE', 'DESCONOCIDO', 'SOLTERO', 'DIVORCIADO',
        'VIUDO'])
NIVEL_ACADEMICO_3 = st.selectbox(label="Nivel Académico",
                               options=['NO INDICA', 'BACHILLERATO', 'PREGRADO - TÉCNICO PROFESIONAL',
        'PREGRADO - TECNOLÓGICO', 'PREGRADO - PROFESIONAL', 'PRIMARIA',
        'POSTGRADO - MAESTRIA', 'NINGUNO', 'POSTGRADO - ESPECIALIZACIÓN',
        'POSTGRADO - DOCTORADO', '(NO REGISTRA)', 'SIN PROFESIÓN'])
SUB_AREA_CONOCIMIENTO_4 = st.selectbox(label="Sub Área de Conocimiento", 
                                     options=['CONTADURÍA PÚBLICA', 'NINGUNA', 'EDUCACIÓN', 'MÚSICA',
        'NO INDICA', 'ADMINISTRACIÓN', 'INGENIERÍA QUÍMICA Y AFINES',
        'INGENIERÍA INDUSTRIAL Y AFINES',
        'INGENIERÍA EN SISTEMAS, TELEMÁTICA Y AFINES', 'DERECHO Y AFINES',
        'MEDICINA', 'ARQUITECTURA', 'INGENIERÍA CIVIL Y AFINES',
        'OTROS ESTUDIOS EN CIENCIAS SOCIALES Y HUMANAS',
        'OTRO PROGRAMA DE BELLAS ARTES',
        'PERIODISMO, COMUNICACIÓN SOCIAL Y AFINES',
        'INGENIERÍA DE PETRÓLEOS',
        'INGENIERÍA ELECTRÓNICA, TELECOMUNICACIONES Y AFINES',
        'ENFERMERÍA', 'PSICOLOGÍA Y AFINES', 'PUBLICIDAD Y AFINES',
        'DISEÑO', 'OTRO PROGRAMA DE SALUD',
        'INGENIERÍA AGROINDUSTRIAL, ALIMENTOS Y AFINES', 'AVIACIÓN',
        'AGRONOMÍA', 'INGENIERÍA MECÁNICA Y AFINES', 'OTRAS INGENIERÍAS',
        'ARTES PLÁSTICAS, VISUALES Y AFINES',
        'LENGUAS MODERNAS, FILOLOGÍA, LINGÜÍSTICA Y AFINES', 'ODONTOLOGÍA',
        'ECONOMÍA', 'QUÍMICA Y AFINES', 'INGENIERÍA ELÉCTRICA Y AFINES',
        'ANTROPOLOGÍA O ARTES LIBERALES',
        'INGENIERÍA AMBIENTAL, SANITARIA Y AFINES',
        'SALUD OCUPACIONAL (HSEQ)', 'SOCIOLOGÍA, TRABAJO SOCIAL Y AFINES',
        'FILOSOFÍA, TEOLOGÍA Y AFINES',
        'INGENIERÍA ADMINISTRATIVA Y AFINES', 'COCINA Y CULINARIA',
        'MEDICINA VETERINARIA', 'TERAPIAS', 'NUTRICIÓN Y DIETÉTICA',
        'INSTRUMENTACIÓN QUIRÚRGICA',
        'CIENCIA POLÍTICA Y/O RELACIONES INTERNACIONALES',
        'MATEMÁTICAS, ESTADÍSTICA Y AFINES', 'GEOGRAFÍA O HISTORIA',
        'BIOLOGÍA, MICROBIOLOGÍA Y AFINES', 'BIBLIOTECOLOGÍA',
        '(NO REGISTRA)', 'FÍSICA',
        'DEPORTES, EDUCACIÓN FÍSICA Y RECREACIÓN', 'ZOOTECNIA',
        'OTROS PROGRAMAS DE CIENCIAS NATURALES', 'FORMACIÓN MILITAR',
        'SALUD PÚBLICA', 'ARTES DRAMÁTICAS Y REPRESENTATIVAS',
        'INGENIERÍA BIOMÉDICA Y AFINES',
        'INGENIERÍA AGRÍCOLA, FORESTAL Y AFINES', 'BACTERIOLOGÍA',
        'INGENIERÍA DE MINAS, METALURGIA Y AFINES', 'OPTOMETRÍA',
        'GEOLOGÍA', 'INGENIERÍA AGRONÓMICA, PECUARIA Y AFINES'])

request_data = [
{
        "AREA_CONOCIMIENTO": AREA_CONOCIMIENTO_1 ,
        "ESTADO_CIVIL": ESTADO_CIVIL_2,
        "NIVEL_ACADEMICO": NIVEL_ACADEMICO_3,
        "SUB_AREA_CONOCIMIENTO": SUB_AREA_CONOCIMIENTO_4
    }
]

url_api="http://127.0.0.1:8000/predict"
data = str(request_data).replace("'", '"')
prediccion = requests.post(url=url_api, data=request_data).text
st.metric(value=pd.read_json(prediccion)["detail"][0] ,label="sdfsd")


