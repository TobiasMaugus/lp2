from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model.usuarios import Usuarios
from model.atividades import Atividades
from model.comentarios import Comentarios
from model.curtidas import Curtidas

engine = create_engine("mysql+pymysql://primeiro_20202017120:cefetMG20202017120@primeiro.cefetvga.pro.br/primeiro_20202017120?charset=utf8mb4", echo=True)

Session = sessionmaker(bind=engine)
session = Session()

def createUsuarios():
    user1 = Usuarios(email='usu1@usu.com', senha='123')
    user2 = Usuarios(email='usu2@usu.com', senha='234')
    user3 = Usuarios(email='usu3@usu.com', senha='456')

    session.add(user1)
    session.add(user2)
    session.add(user3)
    session.commit()


def createAtividades():

    atividade1 = Atividades(hora_inicio='2011-03-15 12:05:57', hora_termino='2011-03-15 12:10:57',
    km_percorridos = 10, tipo='corrida', local='praia', usuarios_id=1)

    atividade2 = Atividades(hora_inicio='2011-04-15 12:15:50', hora_termino='2011-04-15 12:30:00',
    km_percorridos = 5, tipo='pedalada', local='VGA', usuarios_id=1)

    atividade3 = Atividades(hora_inicio='2011-03-18 13:05:57', hora_termino='2011-03-18 13:50:57',
    km_percorridos = 4, tipo='caminhada', local='VGA', usuarios_id=1)

    atividade4 = Atividades(hora_inicio='2013-03-15 15:05:57', hora_termino='2013-03-15 15:20:57',
    km_percorridos = 10, tipo='corrida', local='praça', usuarios_id=2)

    atividade5 = Atividades(hora_inicio='2013-04-15 18:19:00', hora_termino='2013-04-15 18:30:00',
    km_percorridos = 5, tipo='pedalada', local='VGA', usuarios_id=2)

    atividade6 = Atividades(hora_inicio='2013-10-17 19:09:58', hora_termino='2013-10-17 19:50:57',
    km_percorridos = 4, tipo='caminhada', local='VGA', usuarios_id=2)

    atividade7 = Atividades(hora_inicio='2015-10-15 14:05:57', hora_termino='2015-10-15 14:20:57',
    km_percorridos = 10, tipo='corrida', local='parque', usuarios_id=3)

    atividade8 = Atividades(hora_inicio='2015-04-15 18:20:00', hora_termino='2015-04-15 19:00:00',
    km_percorridos = 5, tipo='pedalada', local='VGA', usuarios_id=3)

    atividade9 = Atividades(hora_inicio='2015-11-17 20:09:58', hora_termino='2015-11-17 20:50:57',
    km_percorridos = 4, tipo='caminhada', local='VGA', usuarios_id=3)

    session.add(atividade1)
    session.add(atividade2)
    session.add(atividade3)
    session.add(atividade4)
    session.add(atividade5)
    session.add(atividade6)
    session.add(atividade7)
    session.add(atividade8)
    session.add(atividade9)
    session.commit()


def createComentarios():

    comentario1 = Comentarios(comentario = 'show', atividades_id = 1, usuarios_id = 1)
    comentario2 = Comentarios(comentario = 'uau', atividades_id = 2, usuarios_id = 3)
    comentario3 = Comentarios(comentario = 'muito bom', atividades_id = 3, usuarios_id = 2)
    comentario4 = Comentarios(comentario = 'muito legal', atividades_id = 4, usuarios_id = 2)

    session.add(comentario1)
    session.add(comentario2)
    session.add(comentario3)
    session.add(comentario4)
    session.commit()


def createCurtidas():

    curtida1 = Curtidas(atividades_id = 1, usuarios_id = 2)
    curtida2 = Curtidas(atividades_id = 1, usuarios_id = 3)
    curtida3 = Curtidas(atividades_id = 2, usuarios_id = 1)
    curtida4 = Curtidas(atividades_id = 2, usuarios_id = 2)
    curtida5 = Curtidas(atividades_id = 3, usuarios_id = 3)
    curtida6 = Curtidas(atividades_id = 3, usuarios_id = 1)
    curtida7 = Curtidas(atividades_id = 4, usuarios_id = 2)
    curtida8 = Curtidas(atividades_id = 4, usuarios_id = 3)
    curtida9 = Curtidas(atividades_id = 5, usuarios_id = 1)
    curtida10 = Curtidas(atividades_id = 5, usuarios_id = 2)
    curtida11 = Curtidas(atividades_id = 6, usuarios_id = 3)
    curtida12 = Curtidas(atividades_id = 6, usuarios_id = 1)
    curtida13 = Curtidas(atividades_id = 7, usuarios_id = 1)
    curtida14 = Curtidas(atividades_id = 7, usuarios_id = 2)
    curtida15 = Curtidas(atividades_id = 8, usuarios_id = 3)
    curtida16 = Curtidas(atividades_id = 8, usuarios_id = 1)
    curtida17 = Curtidas(atividades_id = 9, usuarios_id = 2)
    curtida18 = Curtidas(atividades_id = 9, usuarios_id = 3)

    session.add(curtida1)    
    session.add(curtida2)    
    session.add(curtida3)
    session.add(curtida4)    
    session.add(curtida5)    
    session.add(curtida6)
    session.add(curtida7)    
    session.add(curtida8)    
    session.add(curtida9)
    session.add(curtida10)    
    session.add(curtida11)    
    session.add(curtida12)
    session.add(curtida13)
    session.add(curtida14)    
    session.add(curtida15)    
    session.add(curtida16)
    session.add(curtida17)    
    session.add(curtida18)    
    session.commit()


def readAtividades():
    tuplas = session.query(Atividades).filter(Atividades.local=='VGA').order_by(Atividades.km_percorridos.desc())
    for tupla in tuplas:
        print('id:', tupla.id, 'id_usuario:', tupla.usuarios_id, 'quilometragem:',tupla.km_percorridos, 'inicio:', tupla.hora_inicio, 'fim:', tupla.hora_termino)


def updateUsuarios():
    user = session.query(Usuarios).filter(Usuarios.email=='usu1@usu.com').one()
    user.senha = 'senhausu1'
    session.commit()

def deleteAtividades():
    user = session.query(Usuarios).filter(Usuarios.email=='usu2@usu.com').one()
    numero_id = user.id
    tuplas = session.query(Atividades).filter(Atividades.local=='VGA').filter(Atividades.usuarios_id==numero_id)
    for tupla in tuplas:
        session.delete(tupla)
    session.commit()


# deleteAtividades()        
# createUsuarios()
# createAtividades()
# createComentarios()
# createCurtidas()
# readAtividades()
# updateUsuarios()

