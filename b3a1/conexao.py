import sqlalchemy as db


engine = db.create_engine("mysql+pymysql://primeiro_20202017120:cefetMG20202017120@primeiro.cefetvga.pro.br/primeiro_20202017120?charset=utf8mb4")
connection = engine.connect()