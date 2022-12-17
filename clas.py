from pydantic import BaseModel as PydanticBaseModel
from pydantic import Field
from typing import Literal
import joblib
import pandas as pd
from fastapi import HTTPException




# Una variable binaria puede ser:
# binaria: int = Field(ge=0, le=1)
# O, binaria: bool
class ModelInput(PydanticBaseModel):
    '''
    Clase que define las entradas del modelo
    
    '''
    AREA_CONOCIMIENTO: Literal['ECONOMIA ADMINISTRACION CONTADURIA Y AFINES', 'NINGUNA',
        'CIENCIAS DE LA EDUCACION', 'BELLAS ARTES', 'NO INDICA',
        'INGENIERÍA, ARQUITECTURA Y AFINES', 'CIENCIAS SOCIALES Y HUMANAS',
        'CIENCIAS DE LA SALUD', 'AGRONOMÍA, VETERINARIA Y AFINES',
        'MATEMATICAS Y CIENCIAS NATURALES', 'NO REGISTRA',
        'COCINA Y CULINARIA', 'AGRONOMIA VETERINARIA Y ZOOTECNIA',
        'AVIACION']
    ESTADO_CIVIL: Literal['CASADO', 'UNION_LIBRE', 'DESCONOCIDO', 'SOLTERO', 'DIVORCIADO',
        'VIUDO']
    NIVEL_ACADEMICO: Literal['NO INDICA', 'BACHILLERATO', 'PREGRADO - TÉCNICO PROFESIONAL',
        'PREGRADO - TECNOLÓGICO', 'PREGRADO - PROFESIONAL', 'PRIMARIA',
        'POSTGRADO - MAESTRIA', 'NINGUNO', 'POSTGRADO - ESPECIALIZACIÓN',
        'POSTGRADO - DOCTORADO', '(NO REGISTRA)', 'SIN PROFESIÓN']
    SUB_AREA_CONOCIMIENTO: Literal['CONTADURÍA PÚBLICA', 'NINGUNA', 'EDUCACIÓN', 'MÚSICA',
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
        'GEOLOGÍA', 'INGENIERÍA AGRONÓMICA, PECUARIA Y AFINES']
    
    

    # OPCIONAL: Poner el ejemplo para que en la documentación ya puedan de una lanzar la predicción.
    class Config:
        schema_extra = {
            "example": {
                'AREA_CONOCIMIENTO': 'ECONOMIA ADMINISTRACION CONTADURIA Y AFINES',
                'ESTADO_CIVIL': 'CASADO',
                'NIVEL_ACADEMICO': 'NO INDICA',
                'SUB_AREA_CONOCIMIENTO': 'CONTADURÍA PÚBLICA'
            }
        }


class ModelOutput(PydanticBaseModel):
    '''
    Clase que define las salidas del modelo
    '''
    PAIS: Literal['ESPAÑA', 'VENEZUELA', 'ESTADOS UNIDOS', 'BELGICA', 'CANADA',
        'CHILE', 'SUIZA', 'PANAMA', 'PERU', 'FRANCIA', 'ECUADOR',
        'FEDERACION DE RUSIA', 'AUSTRALIA', 'LIBANO', 'TAILANDIA',
        'MEXICO', 'PORTUGAL', 'COSTA RICA', 'JAPON', 'CURAÇAO', 'BRASIL',
        'GUATEMALA', 'REINO UNIDO', 'ITALIA', 'ARGENTINA', 'ARUBA',
        'REPUBLICA DOMINICANA', 'TURQUIA', 'ALEMANIA', 'ISRAEL',
        'HONG KONG', 'BOLIVIA', 'CUBA', 'PAISES BAJOS', 'KENIA',
        'BOSNIA Y HERZEGOVINA', 'NUEVA ZELANDA', 'HONDURAS', 'POLONIA',
        'PARAGUAY', 'QATAR', 'CHINA', 'AUSTRIA', 'LETONIA', 'SUECIA',
        'ANDORRA', 'EMIRATOS ARABES UNIDOS', 'MARRUECOS', 'BULGARIA',
        'URUGUAY', 'CROACIA', 'LUXEMBURGO', 'ST. MAARTEN', 'BONAIRE',
        'RUSIA', 'NORUEGA', 'EL SALVADOR', 'IRLANDA', 'SURINAM',
        'FILIPINAS', 'INDIA', 'TRINIDAD Y TOBAGO', 'CHIPRE', 'MALTA',
        'HUNGRIA', 'GUYANA FRANCESA', 'VIET NAM', 'DINAMARCA', 'GUADALUPE',
        'NIGERIA', 'COREA, REPUBLICA DE', 'PALESTINA', 'INDONESIA',
        'AFGANISTAN', 'ANTILLAS HOLANDESAS', 'REPUBLICA CHECA',
        'SUDAN DEL SUR', 'JORDANIA', 'SINGAPUR', 'JAMAICA', 'MOZAMBIQUE',
        'GRECIA', 'FINLANDIA', 'ARABIA SAUDITA', 'SUDAFRICA', 'AZERBAIYAN',
        'ANGOLA', 'NIGER', 'UCRANIA', 'RUMANIA', 'BANGLADESH', 'MALASIA',
        'BAHREIN', 'NICARAGUA', 'BENIN', 'ARGELIA', 'EGIPTO', 'LIBERIA',
        'LAO, REPUBLIC DEMOCRATICA POPULAR DE', 'HAITI', 'BAHAMAS',
        'GUINEA ECUATORIAL', 'GABON', 'MOLDOVA, REPUBLICA DE', 'MALAWI',
        'SAINT-MARTIN', 'KUWAIT', 'REPUBLICA DE CHINA-TAIWAN', 'SRI LANKA',
        'BERMUDAS', 'ANTIGUA Y BARBUDA', 'CONGO', 'CAMERUN', 'BIELORRUSIA',
        'ISLANDIA', 'ESLOVAQUIA', 'OMAN', 'LITUANIA',
        'CONGO, REPUBLICA DEMOCRATICA DE', 'ESTONIA', 'GHANA', 'TUNEZ',
        'IRAN, REPUBLICA ISLAMICA DE', 'DESCONOCIDO', 'ESLOVENIA',
        'MYANMAR', 'SAN MARINO', 'CAMBOYA', 'RUANDA', 'MONACO', 'SENEGAL',
        'SIERRA LEONA', 'ALBANIA', 'CABO VERDE', 'IRAK', 'MALI', 'SERBIA',
        'MACEDONIA, EX REPUBLICA YUGOSLAVA DE', 'KOSOVO',
        'TANZANIA, REPUBLICA UNIDA DE', 'SUAZILANDIA', 'PAKISTAN',
        'UGANDA', 'ETIOPIA', 'MONGOLIA', 'BARBADOS', 'BELICE', 'GUYANA',
        'GUINEA', 'GEORGIA', 'VIETNAM', 'UZBEKISTAN', 'MARTINICA',
        'VANUATU', 'MADAGASCAR', 'ARMENIA', 'KAZAJSTAN', 'BOTSUANA',
        'MAURICIO', 'COSTA DE MARFIL', 'BRUNEI DARUSSALAM',
        'REPUBLICA ARABE SIRIA', 'MACAO', 'SANTO TOME Y PRINCIPE',
        'LIECHTENSTEIN', 'YEMEN', 'GUINEA-BISSAU', 'SIRIA',
        'CHINA, REPÚBLICA POPULAR', 'SUDAN', 'KIRGUISTAN',
        'COREA, REPUBLICA DEMOCRATICA POPULAR DE', 'DOMINICA',
        'ISLAS COMOROS', 'MONTENEGRO', 'NUEVA CALEDONIA',
        'ISLAS VIRGENES BRITANICAS', 'SANTA LUCIA', 'PAPUA NUEVA GUINEA',
        'GRANADA', 'NAMIBIA', 'GROENLANDIA', 'MALDIVAS',
        'SAINT KITTS Y NEVIS', 'POLINESIA FRANCESA', 'BURKINA FASO',
        'ZAMBIA', 'BURUNDI']

    class Config:
        schema_extra = {
            "example": {
                'PAIS': 'ESPAÑA'
            }
        }


class APIModelBackEnd():
    '''
    Esta clase maneja el back end de nuestro modelo de Machine Learning para la API en FastAPI
    '''

    def __init__(self,AREA_CONOCIMIENTO,ESTADO_CIVIL,NIVEL_ACADEMICO,SUB_AREA_CONOCIMIENTO):
        '''
        Este método se usa al instanciar las clases

        Aquí, hacemos que pida los mismos parámetros que tenemos en ModelInput.

        '''
        
        self.AREA_CONOCIMIENTO = AREA_CONOCIMIENTO
        self.ESTADO_CIVIL = ESTADO_CIVIL
        self.NIVEL_ACADEMICO = NIVEL_ACADEMICO
        self.SUB_AREA_CONOCIMIENTO = SUB_AREA_CONOCIMIENTO
        

    def _load_model(self, model_filename: str = 'modelR2.pkl'):
        '''
        Clase para cargar el modelo. Es una forma exótica de correr joblib.load pero teniendo funcionalidad con la API.
        Este método seguramente no lo van a cambiar, y si lo cambian, cambian el valor por defecto del string
        '''
        # Asignamos a un atributo el nombre del archivo
        self.model_filename = model_filename
        try:
            # Se intenta cargar el modelo
            self.model = joblib.load(self.model_filename)
        except Exception:
            # Si hay un error, se levanda una Exception de HTTP diciendo que no se encontró el modelo
            raise HTTPException(status_code=404, detail=f'Modelo con el nombre {self.model_filename} no fue encontrado')
        # Si todo corre ok, imprimimos que cargamos el modelo
        print(f"El modelo '{self.model_filename}' fue cargado exitosamente")

    def _prepare_data(self):
        '''
        Clase de preparar lo datos.
        Este método convierte las entradas en los datos que tenían en X_train y X_test.

        Miren el orden de las columnas de los datos antes de su modelo.
        Tienen que recrear ese orden, en un dataframe de una fila.

        '''
        # Pueden manejar así las variables categoricas.
        # Revisen los X!!! De eso depende que valores hay aquí.
        # Para ver más o menos que valores pueden ser, en un data frame se le aplico pd.get_dummies, corran algo como:
        # X_test[[col for col in X_test.columns if "nombre de columna" in col]].drop_duplicates()
        
        f2 = ['AREA_CONOCIMIENTO_AGRONOMIA VETERINARIA Y ZOOTECNIA',
        'AREA_CONOCIMIENTO_AGRONOMÍA, VETERINARIA Y AFINES',
        'AREA_CONOCIMIENTO_AVIACION', 'AREA_CONOCIMIENTO_BELLAS ARTES',
        'AREA_CONOCIMIENTO_CIENCIAS DE LA EDUCACION',
        'AREA_CONOCIMIENTO_CIENCIAS DE LA SALUD',
        'AREA_CONOCIMIENTO_CIENCIAS SOCIALES Y HUMANAS',
        'AREA_CONOCIMIENTO_COCINA Y CULINARIA',
        'AREA_CONOCIMIENTO_ECONOMIA ADMINISTRACION CONTADURIA Y AFINES',
        'AREA_CONOCIMIENTO_INGENIERÍA, ARQUITECTURA Y AFINES',
        'AREA_CONOCIMIENTO_MATEMATICAS Y CIENCIAS NATURALES',
        'AREA_CONOCIMIENTO_NINGUNA', 'AREA_CONOCIMIENTO_NO INDICA',
        'AREA_CONOCIMIENTO_NO REGISTRA', 'ESTADO_CIVIL_CASADO',
        'ESTADO_CIVIL_DESCONOCIDO', 'ESTADO_CIVIL_DIVORCIADO',
        'ESTADO_CIVIL_SOLTERO', 'ESTADO_CIVIL_UNION_LIBRE',
        'ESTADO_CIVIL_VIUDO', 'NIVEL_ACADEMICO_(NO REGISTRA)',
        'NIVEL_ACADEMICO_BACHILLERATO', 'NIVEL_ACADEMICO_NINGUNO',
        'NIVEL_ACADEMICO_NO INDICA', 'NIVEL_ACADEMICO_POSTGRADO - DOCTORADO',
        'NIVEL_ACADEMICO_POSTGRADO - ESPECIALIZACIÓN',
        'NIVEL_ACADEMICO_POSTGRADO - MAESTRIA',
        'NIVEL_ACADEMICO_PREGRADO - PROFESIONAL',
        'NIVEL_ACADEMICO_PREGRADO - TECNOLÓGICO',
        'NIVEL_ACADEMICO_PREGRADO - TÉCNICO PROFESIONAL',
        'NIVEL_ACADEMICO_PRIMARIA', 'NIVEL_ACADEMICO_SIN PROFESIÓN',
        'SUB_AREA_CONOCIMIENTO_(NO REGISTRA)',
        'SUB_AREA_CONOCIMIENTO_ADMINISTRACIÓN',
        'SUB_AREA_CONOCIMIENTO_AGRONOMÍA',
        'SUB_AREA_CONOCIMIENTO_ANTROPOLOGÍA O ARTES LIBERALES',
        'SUB_AREA_CONOCIMIENTO_ARQUITECTURA',
        'SUB_AREA_CONOCIMIENTO_ARTES DRAMÁTICAS Y REPRESENTATIVAS',
        'SUB_AREA_CONOCIMIENTO_ARTES PLÁSTICAS, VISUALES Y AFINES',
        'SUB_AREA_CONOCIMIENTO_AVIACIÓN', 'SUB_AREA_CONOCIMIENTO_BACTERIOLOGÍA',
        'SUB_AREA_CONOCIMIENTO_BIBLIOTECOLOGÍA',
        'SUB_AREA_CONOCIMIENTO_BIOLOGÍA, MICROBIOLOGÍA Y AFINES',
        'SUB_AREA_CONOCIMIENTO_CIENCIA POLÍTICA Y/O RELACIONES INTERNACIONALES',
        'SUB_AREA_CONOCIMIENTO_COCINA Y CULINARIA',
        'SUB_AREA_CONOCIMIENTO_CONTADURÍA PÚBLICA',
        'SUB_AREA_CONOCIMIENTO_DEPORTES, EDUCACIÓN FÍSICA Y RECREACIÓN',
        'SUB_AREA_CONOCIMIENTO_DERECHO Y AFINES',
        'SUB_AREA_CONOCIMIENTO_DISEÑO', 'SUB_AREA_CONOCIMIENTO_ECONOMÍA',
        'SUB_AREA_CONOCIMIENTO_EDUCACIÓN', 'SUB_AREA_CONOCIMIENTO_ENFERMERÍA',
        'SUB_AREA_CONOCIMIENTO_FILOSOFÍA, TEOLOGÍA Y AFINES',
        'SUB_AREA_CONOCIMIENTO_FORMACIÓN MILITAR',
        'SUB_AREA_CONOCIMIENTO_FÍSICA',
        'SUB_AREA_CONOCIMIENTO_GEOGRAFÍA O HISTORIA',
        'SUB_AREA_CONOCIMIENTO_GEOLOGÍA',
        'SUB_AREA_CONOCIMIENTO_INGENIERÍA ADMINISTRATIVA Y AFINES',
        'SUB_AREA_CONOCIMIENTO_INGENIERÍA AGROINDUSTRIAL, ALIMENTOS Y AFINES',
        'SUB_AREA_CONOCIMIENTO_INGENIERÍA AGRONÓMICA, PECUARIA Y AFINES',
        'SUB_AREA_CONOCIMIENTO_INGENIERÍA AGRÍCOLA, FORESTAL Y AFINES',
        'SUB_AREA_CONOCIMIENTO_INGENIERÍA AMBIENTAL, SANITARIA Y AFINES',
        'SUB_AREA_CONOCIMIENTO_INGENIERÍA BIOMÉDICA Y AFINES',
        'SUB_AREA_CONOCIMIENTO_INGENIERÍA CIVIL Y AFINES',
        'SUB_AREA_CONOCIMIENTO_INGENIERÍA DE MINAS, METALURGIA Y AFINES',
        'SUB_AREA_CONOCIMIENTO_INGENIERÍA DE PETRÓLEOS',
        'SUB_AREA_CONOCIMIENTO_INGENIERÍA ELECTRÓNICA, TELECOMUNICACIONES Y AFINES',
        'SUB_AREA_CONOCIMIENTO_INGENIERÍA ELÉCTRICA Y AFINES',
        'SUB_AREA_CONOCIMIENTO_INGENIERÍA EN SISTEMAS, TELEMÁTICA Y AFINES',
        'SUB_AREA_CONOCIMIENTO_INGENIERÍA INDUSTRIAL Y AFINES',
        'SUB_AREA_CONOCIMIENTO_INGENIERÍA MECÁNICA Y AFINES',
        'SUB_AREA_CONOCIMIENTO_INGENIERÍA QUÍMICA Y AFINES',
        'SUB_AREA_CONOCIMIENTO_INSTRUMENTACIÓN QUIRÚRGICA',
        'SUB_AREA_CONOCIMIENTO_LENGUAS MODERNAS, FILOLOGÍA, LINGÜÍSTICA Y AFINES',
        'SUB_AREA_CONOCIMIENTO_MATEMÁTICAS, ESTADÍSTICA Y AFINES',
        'SUB_AREA_CONOCIMIENTO_MEDICINA',
        'SUB_AREA_CONOCIMIENTO_MEDICINA VETERINARIA',
        'SUB_AREA_CONOCIMIENTO_MÚSICA', 'SUB_AREA_CONOCIMIENTO_NINGUNA',
        'SUB_AREA_CONOCIMIENTO_NO INDICA',
        'SUB_AREA_CONOCIMIENTO_NUTRICIÓN Y DIETÉTICA',
        'SUB_AREA_CONOCIMIENTO_ODONTOLOGÍA', 'SUB_AREA_CONOCIMIENTO_OPTOMETRÍA',
        'SUB_AREA_CONOCIMIENTO_OTRAS INGENIERÍAS',
        'SUB_AREA_CONOCIMIENTO_OTRO PROGRAMA DE BELLAS ARTES',
        'SUB_AREA_CONOCIMIENTO_OTRO PROGRAMA DE SALUD',
        'SUB_AREA_CONOCIMIENTO_OTROS ESTUDIOS EN CIENCIAS SOCIALES Y HUMANAS',
        'SUB_AREA_CONOCIMIENTO_OTROS PROGRAMAS DE CIENCIAS NATURALES',
        'SUB_AREA_CONOCIMIENTO_PERIODISMO, COMUNICACIÓN SOCIAL Y AFINES',
        'SUB_AREA_CONOCIMIENTO_PSICOLOGÍA Y AFINES',
        'SUB_AREA_CONOCIMIENTO_PUBLICIDAD Y AFINES',
        'SUB_AREA_CONOCIMIENTO_QUÍMICA Y AFINES',
        'SUB_AREA_CONOCIMIENTO_SALUD OCUPACIONAL (HSEQ)',
        'SUB_AREA_CONOCIMIENTO_SALUD PÚBLICA',
        'SUB_AREA_CONOCIMIENTO_SOCIOLOGÍA, TRABAJO SOCIAL Y AFINES',
        'SUB_AREA_CONOCIMIENTO_TERAPIAS', 'SUB_AREA_CONOCIMIENTO_ZOOTECNIA']
        
        
        df2 = pd.DataFrame(columns=f2,data=[[*[0]*len(f2)]])

        
        columA = [x for x in df2.columns if "AREA_CONOCIMIENTO_" in x and str(self.AREA_CONOCIMIENTO) == x.split('_')[-1]]
        df2[columA] = 1
        columE = [x for x in df2.columns if "ESTADO_CIVIL_" in x and str(self.ESTADO_CIVIL) == x.split('_')[-1]]
        df2[columE] = 1
        columN = [x for x in df2.columns if "NIVEL_ACADEMICO_" in x and str(self.NIVEL_ACADEMICO) == x.split('_')[-1]]
        df2[columN] = 1
        columS = [x for x in df2.columns if "SUB_AREA_CONOCIMIENTO_" in x and str(self.SUB_AREA_CONOCIMIENTO) == x.split('_')[-1]]
        df2[columS] = 1
        
        
        return df2

    def predict(self, y_name: str = 'PAIS'):
        '''
        Clase para predecir.
        Carga el modelo, prepara los datos y predice.

        prediction = pd.DataFrame(self.model.predict(X)).rename(columns={0:y_name})

        '''
        self._load_model()
        X = self._prepare_data()
        prediction = pd.DataFrame(self.model.predict(X)).rename(columns={0: y_name})
        return prediction.to_dict(orient='records')