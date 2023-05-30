from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func, distinct

from genera_tablas import Provincia, Canton, Parroquia, Institucion

from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

consulta = session.query(Institucion).order_by(Institucion.numEstudiantes).filter(
    Institucion.numDocentes > 100).all()

for institucion in consulta:
    print(institucion.id, institucion.nombre_institucion)

print("----------------------")
print("Consulta 2")

consulta2 = session.query(Institucion).order_by(Institucion.numDocentes).filter(
    Institucion.numDocentes > 100).all()

for institucion in consulta2:
    print(institucion.id, institucion.nombre_institucion)