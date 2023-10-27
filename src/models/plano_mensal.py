from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Creating the Inserttable for inserting data into the database


class PlanoMensal(db.Model):
    '''Data for ON/OFF should be dumped in this table.'''

    __tablename__ = 'plano_mensal'
    id_plano = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    descricao = db.Column(db.String(100), nullable=False)
    preco = db.Column(db.Float, nullable=False)

    # method used to represent a class's objects as a string
    def __init__(self, id_plano, nome, descricao, preco):
        self.id_plano = id_plano
        self.nome = nome
        self.descricao = descricao
        self.preco = preco