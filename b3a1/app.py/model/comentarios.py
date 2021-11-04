from sqlalchemy import Column, Integer, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import String



Base = declarative_base()

class Comentarios(Base):

    # indica o nome da tabela no BD
    __tablename__ = 'comentarios'

    id = Column(Integer, Sequence ( 'comentarios_id' ), primary_key=True)
    comentario = Column(String(1000))

    def __repr__(self):
        return f'Comentarios {self.nome}'