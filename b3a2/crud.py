from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model.tabelas import Atividades, Comentarios, Usuarios, Curtidas

engine = create_engine("mysql+pymysql://primeiro_20202017120:cefetMG20202017120@primeiro.cefetvga.pro.br/primeiro_20202017120?charset=utf8mb4", echo=True)

Session = sessionmaker(bind=engine)
session = Session()

def create():
    #!criando usuarios#
    user1 = Usuarios(email='usu1@usu.com', senha='123')
    user2 = Usuarios(email='usu2@usu.com', senha='234')
    user3 = Usuarios(email='usu3@usu.com', senha='456')

    session.add(user1)
    session.add(user2)
    session.add(user3)
    session.commit()

    #!criando atvidades#
    atividade1 = Atividades(hora_inicio='2011-03-15 12:05:57', hora_termino='2011-03-15 12:10:57',
    km_percorridos = 7, tipo='corrida', local='praia', usuarios_id=user1.id)

    atividade2 = Atividades(hora_inicio='2011-04-15 12:15:50', hora_termino='2011-04-15 12:30:00',
    km_percorridos = 2, tipo='pedalada', local='VGA', usuarios_id=user1.id)

    atividade3 = Atividades(hora_inicio='2011-03-18 13:05:57', hora_termino='2011-03-18 13:50:57',
    km_percorridos = 3, tipo='caminhada', local='VGA', usuarios_id=user1.id)

    atividade4 = Atividades(hora_inicio='2013-03-15 15:05:57', hora_termino='2013-03-15 15:20:57',
    km_percorridos = 1, tipo='corrida', local='praça', usuarios_id=user2.id)

    atividade5 = Atividades(hora_inicio='2013-04-15 18:19:00', hora_termino='2013-04-15 18:30:00',
    km_percorridos = 8, tipo='pedalada', local='VGA', usuarios_id=user2.id)

    atividade6 = Atividades(hora_inicio='2013-10-17 19:09:58', hora_termino='2013-10-17 19:50:57',
    km_percorridos = 9, tipo='caminhada', local='VGA', usuarios_id=user2.id)

    atividade7 = Atividades(hora_inicio='2015-10-15 14:05:57', hora_termino='2015-10-15 14:20:57',
    km_percorridos = 10, tipo='corrida', local='parque', usuarios_id=user3.id)

    atividade8 = Atividades(hora_inicio='2015-04-15 18:20:00', hora_termino='2015-04-15 19:00:00',
    km_percorridos = 5, tipo='pedalada', local='VGA', usuarios_id=user3.id)

    atividade9 = Atividades(hora_inicio='2015-11-17 20:09:58', hora_termino='2015-11-17 20:50:57',
    km_percorridos = 4, tipo='caminhada', local='VGA', usuarios_id=user3.id)

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

    #!criando comentarios#
    comentario1 = Comentarios(comentario = 'show', atividades_id = atividade1.id, usuarios_id = user3.id)
    comentario2 = Comentarios(comentario = 'uau', atividades_id = atividade2.id, usuarios_id = user3.id)
    comentario3 = Comentarios(comentario = 'muito bom', atividades_id = atividade3.id, usuarios_id = user1.id)
    comentario4 = Comentarios(comentario = 'muito legal', atividades_id = atividade4.id, usuarios_id = user1.id)

    session.add(comentario1)
    session.add(comentario2)
    session.add(comentario3)
    session.add(comentario4)
    session.commit()

    #!criando curtidas#
    curtida1 = Curtidas(atividades_id = atividade1.id, usuarios_id = user1.id)
    curtida2 = Curtidas(atividades_id = atividade1.id, usuarios_id = user2.id)
    curtida3 = Curtidas(atividades_id = atividade2.id, usuarios_id = user3.id)
    curtida4 = Curtidas(atividades_id = atividade2.id, usuarios_id = user1.id)
    curtida5 = Curtidas(atividades_id = atividade3.id, usuarios_id = user2.id)
    curtida6 = Curtidas(atividades_id = atividade3.id, usuarios_id = user3.id)
    curtida7 = Curtidas(atividades_id = atividade4.id, usuarios_id = user1.id)
    curtida8 = Curtidas(atividades_id = atividade4.id, usuarios_id = user2.id)
    curtida9 = Curtidas(atividades_id = atividade5.id, usuarios_id = user3.id)
    curtida11 = Curtidas(atividades_id = atividade6.id, usuarios_id = user1.id)
    curtida12 = Curtidas(atividades_id = atividade6.id, usuarios_id = user2.id)
    curtida13 = Curtidas(atividades_id = atividade7.id, usuarios_id = user3.id)
    curtida14 = Curtidas(atividades_id = atividade7.id, usuarios_id = user1.id)
    curtida15 = Curtidas(atividades_id = atividade8.id, usuarios_id = user2.id)
    curtida16 = Curtidas(atividades_id = atividade8.id, usuarios_id = user3.id)
    curtida17 = Curtidas(atividades_id = atividade9.id, usuarios_id = user1.id)
    curtida18 = Curtidas(atividades_id = atividade9.id, usuarios_id = user2.id)
    curtida10 = Curtidas(atividades_id = atividade5.id, usuarios_id = user3.id)

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
    tuplas = session.query(Atividades).filter(Atividades.local=='VGA').filter(Atividades.usuarios_id==user.id)
    for tupla in tuplas:
        session.delete(tupla)
    session.commit()


#!chamada das funções#
# create()
# readAtividades()
# updateUsuarios()
# deleteAtividades()

