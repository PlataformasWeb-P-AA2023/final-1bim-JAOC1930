from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func, distinct

from genera_tablas import Provincia, Canton, Parroquia, Institucion

from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

consulta = session.query(Institucion).join(Parroquia).order_by(Parroquia.nombreParroquia).filter(
    Parroquia.id == Institucion.parroquia_id, Institucion.numDocentes > 40, 
    Institucion.tipoEducacion == "Educación regular").all()

for institucion in consulta:
    print(institucion.id, institucion.nombre_institucion)

print("-----------------------")
print("Consulta 2\n")

consulta2 = session.query(Institucion).order_by(Institucion.sostenimiento).filter(
    Institucion.codigo_Distrito != "11D04").all()

for institucion in consulta2:
    print(institucion.id, institucion.nombre_institucion)