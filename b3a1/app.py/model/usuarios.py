from sqlalchemy import Column, Integer, String, Date, Sequence
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Usuarios(Base):

    # indica o nome da tabela no BD
    __tablename__ = 'usuarios'

    id = Column(Integer, Sequence ( 'usuarios_id' ), primary_key=True)
    email = Column(String(255),unique=True, nullable=False)
    senha = Column(String(45), nullable=False)


    def __repr__(self):
        return f'Usuario {self.nome}'
