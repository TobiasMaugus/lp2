from sqlalchemy import Column, Integer, String, Date, Sequence, Time
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Atividades(Base):

    __tablename__ = 'atividades'

    id = Column(Integer, Sequence ( 'atividades_id' ), primary_key=True)
    data_atv = Column(Date, nullable=False)
    hora_inicio = Column(Time, nullable=False)
    hora_termino = Column(Time, nullable=False)
    km_percorridos = Column(Integer, nullable=False)
    tipo = Column(String(50), nullable=False)
    local = Column(String(100), nullable=False)
    usuarios_id = Column(Integer)


    def __repr__(self):
        return f'Atividades {self.nome}'