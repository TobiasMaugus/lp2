from sqlalchemy import Column, Integer, String, Date, Sequence
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Usuario(Base):

    # indica o nome da tabela no BD
    __tablename__ = 'usuario'

    id = Column(Integer, Sequence ( 'user_id_seq' ), primary_key=True)
    email = Column(String(255),unique=True, nullable=False)
    senha = Column(String(45), nullable=False)

    nome = Column(String(25))
    data_nascimento = Column(Date)



    def __repr__(self):
        return f'Usuario {self.nome}'

    #uma pratica comum eh criar as queries como um metodo estatico @classmethod
    @classmethod
    def find_by_email(cls, session, email):
        return session.query(cls).filter_by(email=email).one()