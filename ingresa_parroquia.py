from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pandas as pd

from genera_tablas import Canton, Parroquia

from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

data = pd.read_csv('data/Listado-Instituciones-Educativas.csv', delimiter='|')

columnas_especificas = data[['Código División Política Administrativa  Cantón', \
                             'Código División Política Administrativa  Parroquia', 'Parroquia']]
valores_unicos = columnas_especificas.drop_duplicates()

print(valores_unicos)

for index, row in valores_unicos.iterrows():
    codigo_divisionC = row['Código División Política Administrativa  Cantón']
    codigo_division = row['Código División Política Administrativa  Parroquia']
    parroquia1 = row['Parroquia']

    canton = session.query(Canton).filter_by(codigoCanton=codigo_divisionC).one()

    print(codigo_divisionC,codigo_division, parroquia1)

    parroquia = Parroquia(codigoParroquia=int(codigo_division), nombreParroquia=parroquia1, cantones=canton)
    session.add(parroquia)

session.commit()
