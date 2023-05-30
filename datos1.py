from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_

from genera_tablas import Provincia, Canton, Parroquia, Institucion

from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

consulta = session.query(Institucion).join(Parroquia).filter(Parroquia.codigoParroquia == 110553).all()

for institucion in consulta:
    print(institucion.nombre_institucion)


print("-----------------------------------------")
print("Consulta2\n")

consulta2 = session.query(Institucion).join(Parroquia).join(Canton).join(Provincia).filter(
    Institucion.parroquia_id == Parroquia.id,
    Parroquia.canton_id == Canton.id,
    Canton.provincia_id == Provincia.id,
    Provincia.nombreProvincia == "EL ORO").all()

for institucion2 in consulta2:
    print(institucion2.nombre_institucion)


print("-----------------------------------------")
print("Consulta3\n")

consulta3 = session.query(Institucion).join(Parroquia).join(Canton).filter(
    Canton.nombreCanton == "PORTOVELO"
).all()

for institucion3 in consulta3:
    print(institucion3.nombre_institucion)


print("-----------------------------------------")
print("Consulta4\n")

consulta4 = session.query(Institucion).join(Parroquia).join(Canton).filter(
    Canton.nombreCanton == "ZAMORA"
).all()

for institucion4 in consulta4:
    print(institucion4.nombre_institucion)