from sqlalchemy import Column, Integer, String, Sequence, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import DateTime

Base = declarative_base()

class b4a1usuarios(Base):

    __tablename__ = 'b4a1usuarios'

    id = Column(Integer, Sequence ( 'usuarios_id' ), primary_key=True)
    nome = Column(String(255), nullable=False)
    email = Column(String(50), nullable=False)
    senha = Column(String(50), nullable=False)
    jogos = relationship("b4a1compras",backref='b4a1usuarios', lazy=True)
    


class b4a1compras(Base):

    __tablename__ = 'b4a1compras'

    id = Column(Integer, Sequence ('b4a1compras_id'), primary_key=True)
    data_compra = Column(DateTime, nullable=False)
    usuarios_id = Column(Integer, ForeignKey('b4a1usuarios.id'))
    jogos_id = Column(Integer, ForeignKey('b4a1jogos.id'))



class b4a1desenvolvedores(Base):

    __tablename__ = 'b4a1desenvolvedores'

    id = Column(Integer, Sequence ( 'b4a1desenvolvedores_id' ), primary_key=True)
    cnpj = Column(String(20), nullable=False)
    nome = Column(String(100), nullable=False)
    jogos = relationship("b4a1jogos",backref='b4a1desenvolvedores', lazy=True)


class b4a1jogos(Base):

    __tablename__ = 'b4a1jogos'

    id = Column(Integer, Sequence ( 'b4a1jogos_id' ), primary_key=True)
    nome = Column(String(70), nullable=False)
    preco = Column(Float, nullable=False)
    rating = Column(Float, nullable=False)
    desenvolvedores_id = Column(Integer, ForeignKey('b4a1desenvolvedores.id'))
    usuarios = relationship("b4a1compras",backref='b4a1jogos', lazy=True)