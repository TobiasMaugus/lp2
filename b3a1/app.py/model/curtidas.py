from sqlalchemy import Column, Integer, Sequence, Boolean
from sqlalchemy.ext.declarative import declarative_base



Base = declarative_base()

class Curtidas(Base):

    # indica o nome da tabela no BD
    __tablename__ = 'curtidas'

    id = Column(Integer, Sequence ( 'curtidas_id' ), primary_key=True)
    atividades_id = Column(Integer)
    usuarios_id = Column(Integer)

    def __repr__(self):
        return f'Curtida {self.nome}'