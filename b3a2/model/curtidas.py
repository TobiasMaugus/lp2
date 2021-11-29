from sqlalchemy import Column, Integer, Sequence
from sqlalchemy.ext.declarative import declarative_base



Base = declarative_base()

class Curtidas(Base):

    __tablename__ = 'curtidas'

    id = Column(Integer, Sequence ( 'curtidas_id' ), primary_key=True)
    atividades_id = Column(Integer, nullable=False)
    usuarios_id = Column(Integer, nullable=False)

    def __repr__(self):
        return f'Curtida {self.nome}'