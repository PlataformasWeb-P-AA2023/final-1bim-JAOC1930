from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Column, Integer, String, ForeignKey

from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)

Base = declarative_base()



class Provincia(Base):
    __tablename__ = 'provincia'
    id = Column(Integer, primary_key=True)
    codigoProvincia = Column(Integer, nullable=False)
    nombrePronvicia = Column(String(100))

    canton = relationship("Canton", back_populates="provincia")

    
    def __repr__(self):
        return "Club: nombre=%s deporte=%s fundación=%d" % (
                          self.nombre, 
                          self.deporte, 
                          self.fundacion)

class Canton(Base):
    __tablename__ = 'canton'
    id = Column(Integer, primary_key=True)
    codigoCanton = Column(Integer)
    nombreCanton = Column(String(100), nullable=False)

    provincia_id = Column(Integer, ForeignKey('provincia.id'))

    provincia  = relationship("Provincia", back_populates="canton")

    parroquia = relationship("Parroquia", back_populates="canton")
    
    def __repr__(self):
        return "Jugador: %s - dorsal:%d - posición: %s" % (
                self.nombre, self.dorsal, self.posicion)
    
class Parroquias(Base):
    __tablename__ = 'parroquia'
    id = Column(Integer, primary_key=True)
    codigoParroquia = Column(Integer)
    nombreParroquia = Column(String(100), nullable=False)

    canton_id = Column(Integer, ForeignKey('canton.id'))

    canton = relationship("Canton", back_populates = "parroquia")

class establecimiento(Base):
    __tablename__ = 'establecimiento'
    id = Column(Integer, primary_key=True)
    amie = Column(String(100))
    educacion_id = Column(Integer, ForeignKey('educacion.id'))

    education = relationship("Educacion", back_populates = "establecimiento")

class educacion(Base):
    __tablename__ = 'educacion'
    id = Column(Integer, primary_key=True)
    tipoEducacion = Column(String(100))
    modalidad = Column(String(100))
    jornada = Column(String(100))
    numEstudiante = Column(Integer)
    numDocentes = Column(Integer)

    establecimiento = relationship("Establecimiento", back_populates = "educacion")

class distritos(Base):
    __tablename__ = 'distritos'
    id = Column(Integer, primary_key=True)
    distritos = Column(String(100))


class 

        



Base.metadata.create_all(engine)









