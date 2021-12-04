from sqlalchemy import Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import DateTime

Base = declarative_base()

class Clientes(Base):

    __tablename__ = 'clientes'

    id = Column(Integer, Sequence ( 'clientes_id' ), primary_key=True)
    endereco = Column(String(255), nullable=False)
    telefone = Column(String(15), nullable=False)
    cpf = Column(String(16), unique=True, nullable=False)
    livros = relationship("Compras",backref='Clientes', lazy=True)
    


class Compras(Base):

    __tablename__ = 'compras'

    id = Column(Integer, Sequence ('compras_id'), primary_key=True)
    data_compra = Column(DateTime, nullable=False)
    clientes_id = Column(Integer, ForeignKey('clientes.id'))
    livros_id = Column(Integer, ForeignKey('livros.id'))



class Editoras(Base):

    __tablename__ = 'editoras'

    id = Column(Integer, Sequence ( 'editoras_id' ), primary_key=True)
    endereco = Column(String(255), nullable=False)
    telefone = Column(String(15), nullable=False)
    nome_gerente = Column(String(130), nullable=False)
    livros = relationship("Livros",backref='Editoras', lazy=True)


class Livros(Base):

    __tablename__ = 'livros'

    id = Column(Integer, Sequence ( 'livros_id' ), primary_key=True)
    nome = Column(String(70), nullable=False)
    autor = Column(String(130), nullable=False)
    assunto = Column(String(50), nullable=False)
    isbn = Column(String(20), nullable=False)
    quantidade = Column(Integer, nullable=False)
    editoras_id = Column(Integer, ForeignKey('editoras.id'))
    clientes = relationship("Compras",backref='Livros', lazy=True)