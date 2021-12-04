from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models.tabelas import Clientes, Editoras, Compras, Livros

engine = create_engine("mysql+pymysql://primeiro_20202017120:cefetMG20202017120@primeiro.cefetvga.pro.br/primeiro_20202017120?charset=utf8mb4", echo=True)

Session = sessionmaker(bind=engine)
session = Session()

def create():
    #criando clientes
    cliente1 = Clientes(endereco='Três Pontas', telefone='99877-9089', cpf='890.177.168.97')
    cliente2 = Clientes(endereco='Varginha', telefone='99866-8080', cpf='123.789.190.21')
    cliente3 = Clientes(endereco='Boa esperanca', telefone='8031-9922', cpf='512.513.907.98')
        
    session.add(cliente1)
    session.add(cliente2)
    session.add(cliente3)
    session.commit()

    #criando editoras
    editora1 = Editoras(endereco='Sao paulo', telefone='8922-4002', nome_gerente='Tobias')
    editora2 = Editoras(endereco='Minas Gerais', telefone='3265-2218', nome_gerente='Julia')
    editora3 = Editoras(endereco='Rio de janeiro', telefone='7822-0312', nome_gerente='Taiane')

    session.add(editora1)
    session.add(editora2)
    session.add(editora3)
    session.commit()

    #criando livros
    livro1 = Livros(nome='O pequeno principe', autor='João', assunto='fantasia', 
    isbn='189-8132-90-4', quantidade=8, editoras_id=editora3.id)
    livro2 = Livros(nome='Senhora', autor='Bruno', assunto='romance', 
    isbn='134-8772-78-3', quantidade=5, editoras_id=editora2.id)
    livro3 = Livros(nome='O alquimista', autor='José', assunto='suspense', 
    isbn='680-9120-91-2', quantidade=3, editoras_id=editora1.id)

    session.add(livro1)
    session.add(livro2)
    session.add(livro3)
    session.commit()

    #criando compras
    compra1 = Compras(data_compra='2011-04-15 12:15:50', clientes_id=cliente1.id, livros_id=livro1.id)
    compra2 = Compras(data_compra='2012-05-16 13:16:51', clientes_id=cliente2.id, livros_id=livro2.id)
    compra3 = Compras(data_compra='2021-10-19 11:13:52', clientes_id=cliente3.id, livros_id=livro3.id)

    session.add(compra1)
    session.add(compra2)
    session.add(compra3)
    session.commit()

create()