from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Creating the Inserttable for inserting data into the database


class Instrutor(db.Model):
    '''Data for ON/OFF should be dumped in this table.'''

    __tablename__ = 'instrutor'
    id_instrutor = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)
    sobrenome = db.Column(db.String(50), nullable=False)
    cpf = db.Column(db.String(20), nullable=False)
    data_nascimento = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    senha = db.Column(db.String(50), nullable=False)
    telefone = db.Column(db.String(20), nullable=False)




    def __init__(self, id_instrutor, nome, sobrenome, cpf, data_nascimento, email, senha, telefone):
        self.id_cliente = id_instrutor
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.email = email
        self.senha = senha
        self.telefone =  telefone