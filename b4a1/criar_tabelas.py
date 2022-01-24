from sqlalchemy import *

from models.tabelas import *

engine = create_engine("mysql+pymysql://primeiro_20202017120:cefetMG20202017120@primeiro.cefetvga.pro.br/primeiro_20202017120?charset=utf8mb4", echo=True)

desenvolvedores = b4a1desenvolvedores.__table__
desenvolvedores.create(engine, checkfirst=True)

usuarios = b4a1usuarios.__table__
usuarios.create(engine, checkfirst=True)

jogos = b4a1jogos.__table__
jogos.create(engine, checkfirst=True)

compras = b4a1compras.__table__
compras.create(engine, checkfirst=True)



