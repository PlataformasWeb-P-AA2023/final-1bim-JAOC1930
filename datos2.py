from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func, distinct

from genera_tablas import Provincia, Canton, Parroquia, Institucion

from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

consulta = session.query(Parroquia).join(Institucion).filter(Institucion.jornada == "Matutina y Vespertina").distinct()


for parroquia in consulta:
    print(parroquia.nombreParroquia)

print("----------------------------")
print("Consulta2\n")

num_estudiantes = [448, 450, 451, 454, 458, 459]

consulta2 = session.query(Canton).join(Parroquia).join(Institucion).filter(
    Institucion.parroquia_id == Parroquia.id,
    Parroquia.canton_id == Canton.id,
    Institucion.numEstudiantes.in_(num_estudiantes)
).distinct()

for canton in consulta2:
    print(canton.nombreCanton)
