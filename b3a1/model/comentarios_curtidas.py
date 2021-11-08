from sqlalchemy import Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Comentarios_Curtidas(Base):

    # indica o nome da tabela no BD
    __tablename__ = 'comentarios_curtidas'

    id = Column(Integer, Sequence ( 'comentarios_curtidas_id' ), primary_key=True)
    comentarios_id = Column(Integer)
    curtidas_id = Column(Integer)

    def __repr__(self):
        return f'Comentarios_Curtidas{self.nome}'