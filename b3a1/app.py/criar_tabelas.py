from sqlalchemy import *

from model.usuarios import Usuarios
from model.atividades import Atividades
from model.curtidas import Curtidas
from model.comentarios import Comentarios


engine = create_engine("mysql+pymysql://primeiro_20202017120:cefetMG20202017120@primeiro.cefetvga.pro.br/primeiro_20202017120?charset=utf8mb4", echo=True)

usuario = Usuarios.__table__
usuario.create(engine, checkfirst=True)

atividades = Atividades.__table__
atividades.create(engine, checkfirst=True)

curtidas = Curtidas.__table__
curtidas.create(engine, checkfirst=True)

comentarios = Comentarios.__table__
comentarios.create(engine, checkfirst=True)