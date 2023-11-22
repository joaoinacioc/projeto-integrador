from flask_sqlalchemy import SQLAlchemy
from src.config import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
class Cliente(db.Model):
    '''Data for ON/OFF should be dumped in this table.'''
    __tablename__ = 'cliente'
    id_cliente = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)
    sobrenome = db.Column(db.String(50), nullable=False)
    cpf = db.Column(db.String(20), nullable=False)
    data_nascimento = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    senha = db.Column(db.String(50), nullable=False)
    telefone = db.Column(db.String(20), nullable=False)
    fk_Plano_Mensal_id_plano= db.Column(db.Integer, nullable=False)
    fichas_treino = relationship('Ficha_Treino', back_populates='cliente')
    def __init__(self, nome, sobrenome, cpf, data_nascimento, email, senha, telefone, fk_Plano_Mensal_id_plano):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.email = email
        self.senha = senha
        self.telefone = telefone
        self.fk_Plano_Mensal_id_plano = fk_Plano_Mensal_id_plano