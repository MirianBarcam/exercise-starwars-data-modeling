import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class usuario(Base):
    __tablename__ ='usuario'
    id_usuario = Column(Integer, primary_key=True)
    nombre_usuario = Column(String(30), primary_key=False)
    apellidos_usuario = Column(String(60), primary_key=False)
    contrasena = Column (String(20),primary_key=False)
    email = Column (String(10),primary_key=False)
    favoritos = relationship('favoritos',backref='usuario',lazy=True)


class planetas(Base):
    __tablename__ = 'planetas'
    id_planetas = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    favoritos = relationship('favoritos',backref='planetas',lazy=True)

class personajes(Base):
    __tablename__ = 'personajes'
    id_personajes = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False)
    favoritos = relationship('favoritos',backref='personajes',lazy=True)

class favoritos(Base):
    __tablename__ = 'favoritos'
    id_favoritos =  Column(Integer, primary_key=True)
    fk_usuario = Column(Integer,ForeignKey('usuario.id_usuario'))
    fk_planetas = Column(Integer,ForeignKey('planetas.id_planetas'))
    fk_personajes = Column(Integer,ForeignKey('personajes.id_personajes'))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')