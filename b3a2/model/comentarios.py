from sqlalchemy import Column, Integer, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.sqltypes import String



Base = declarative_base()

class Comentarios(Base):

    __tablename__ = 'comentarios'

    id = Column(Integer, Sequence ( 'comentarios_id' ), primary_key=True)
    comentario = Column(String(1000))
    atividades_id = Column(Integer, nullable=False)
    usuarios_id = Column(Integer, nullable=False)
    
    def __repr__(self):
        return f'Comentarios {self.nome}'