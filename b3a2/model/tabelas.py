from sqlalchemy import Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import DECIMAL, DateTime


Base = declarative_base()

class Atividades(Base):

    __tablename__ = 'atividades'

    id = Column(Integer, Sequence ( 'atividades_id' ), primary_key=True)
    hora_inicio = Column(DateTime, nullable=False)
    hora_termino = Column(DateTime, nullable=False)
    km_percorridos = Column(DECIMAL(10,2), nullable=False)
    tipo = Column(String(50), nullable=False)
    local = Column(String(255), nullable=False)
    usuarios_id = Column(Integer, ForeignKey('usuarios.id'))
    curtida = relationship("Curtidas", backref='Atividades', lazy=True)
    comentario = relationship("Comentarios", backref='Atividades', lazy=True)


    def __repr__(self):
        return f'Atividades {self.nome}'



class Comentarios(Base):

    __tablename__ = 'comentarios'

    id = Column(Integer, Sequence ( 'comentarios_id' ), primary_key=True)
    comentario = Column(String(1000))
    atividades_id = Column(Integer, ForeignKey('atividades.id'))
    usuarios_id = Column(Integer, ForeignKey('usuarios.id'))
    
    def __repr__(self):
        return f'Comentarios {self.nome}'



class Curtidas(Base):

    __tablename__ = 'curtidas'

    id = Column(Integer, Sequence ( 'curtidas_id' ), primary_key=True)
    usuarios_id = Column(Integer, ForeignKey('usuarios.id'))
    atividades_id = Column(Integer, ForeignKey('atividades.id'))

    def __repr__(self):
        return f'Curtida {self.nome}'



class Usuarios(Base):

    __tablename__ = 'usuarios'

    id = Column(Integer, Sequence ( 'usuarios_id' ), primary_key=True)
    email = Column(String(255),unique=True, nullable=False)
    senha = Column(String(45), nullable=False)
    curtida = relationship("Curtidas", backref='Usuarios', lazy=True)
    comentario = relationship("Comentarios", backref='Usuarios', lazy=True)
    atividade = relationship("Atividades", backref='Usuarios', lazy=True)


    def __repr__(self):
        return f'Usuario {self.nome}'