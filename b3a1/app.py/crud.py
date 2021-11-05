from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model.usuarios import Usuarios
from model.atividades import Atividades
from model.comentarios import Comentarios
from model.curtidas import Curtidas

engine = create_engine("mysql+pymysql://primeiro_20202017120:cefetMG20202017120@primeiro.cefetvga.pro.br/primeiro_20202017120?charset=utf8mb4", echo=True)

Session = sessionmaker(bind=engine)
session = Session()

def create():
    user1 = Usuarios(email='tobias@gmail.com', senha='123')
    user2 = Usuarios(email='to@gmail.com', senha='234')
    user3 = Usuarios(email='fael@gmail.com', senha='456')

    session.add(user1)
    session.add(user2)
    session.add(user3)

    atividade1 = Atividades(data_atv='2005-10-09', hora_inicio='10:30', hora_termino='11:30',
    km_percorridos = 10, tipo='corrida', local='praia', usuarios_id=1)

    atividade2 = Atividades(data_atv='2004-11-07', hora_inicio='09:45', hora_termino='10:40',
    km_percorridos = 5, tipo='pedalada', local='praça', usuarios_id=3)

    atividade3 = Atividades(data_atv='2010-06-02', hora_inicio='11:36', hora_termino='13:20',
    km_percorridos = 4, tipo='caminhada', local='parque', usuarios_id=2)

    session.add(atividade1)
    session.add(atividade2)
    session.add(atividade3)

    comentario1 = Comentarios(comentario = 'show', atividades_id = 1, usuarios_id = 1)
    comentario2 = Comentarios(comentario = 'uau', atividades_id = 2, usuarios_id = 3)
    comentario3 = Comentarios(comentario = 'muito bom', atividades_id = 3, usuarios_id = 2)

    session.add(comentario1)
    session.add(comentario2)
    session.add(comentario3)

    curtida1 = Curtidas(atividades_id = 1, usuarios_id = 2)
    curtida2 = Curtidas(atividades_id = 2, usuarios_id = 3)
    curtida3 = Curtidas(atividades_id = 3, usuarios_id = 1)

    session.add(curtida1)    
    session.add(curtida2)    
    session.add(curtida3)    

    session.commit()


create()