from sqlalchemy import *

from models.tabelas import Clientes, Livros, Compras, Editoras



engine = create_engine("mysql+pymysql://primeiro_20202017120:cefetMG20202017120@primeiro.cefetvga.pro.br/primeiro_20202017120?charset=utf8mb4", echo=True)

editora = Editoras.__table__
editora.create(engine, checkfirst=True)


cliente = Clientes.__table__
cliente.create(engine, checkfirst=True)

livro = Livros.__table__
livro.create(engine, checkfirst=True)

compra = Compras.__table__
compra.create(engine, checkfirst=True)



