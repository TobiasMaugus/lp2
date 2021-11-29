from sqlalchemy import Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
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
    usuarios_id = Column(Integer)


    def __repr__(self):
        return f'Atividades {self.nome}'