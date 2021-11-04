from sqlalchemy import create_engine, or_
from sqlalchemy.orm import sessionmaker

from model.usuario import Usuario

engine = create_engine("mysql+pymysql://primeiro_20202017120:cefetMG20202017120@primeiro.cefetvga.pro.br/primeiro_20202017120?charset=utf8mb4", echo=True)

Session = sessionmaker(bind=engine)
session = Session()

def create():
    user1 = Usuario(email='tobias@gmail.com', senha='123')
    user2 = Usuario(email='to@gmail.com', senha='234')
    user3 = Usuario(email='fael@gmail.com', senha='456')

    session.add(user1)
    session.add(user2)
    session.add(user3)

    session.commit()


create()