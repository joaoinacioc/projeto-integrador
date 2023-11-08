from flask_sqlalchemy import SQLAlchemy

from src.config import db


# Creating the Inserttable for inserting data into the database


class Ficha_Treino(db.Model):


    __tablename__ = 'ficha_de_treino'
    id_ficha = db.Column(db.Integer, primary_key=True, autoincrement=True)
    data_criacao = db.Column(db.String(50))
    descricao = db.Column(db.String(50))
    duracao_treino = db.Column(db.String(50))
    ombro_lateral = db.Column(db.String(100))

    ombro_frontal = db.Column(db.String(100))
    supino_reto = db.Column(db.String(100))
    supino_inclinado = db.Column(db.String(100))
    crucifixo = db.Column(db.String(100), primary_key=False)
    puxador_frontal = db.Column(db.String(100))
    puxador_costas = db.Column(db.String(100))
    remada_baixa= db.Column(db.String(100))
    remada_cavalo = db.Column(db.String(100), primary_key=False)
    triceps_corda = db.Column(db.String(100))
    triceps_pulley = db.Column(db.String(100))
    rosca_biceps = db.Column(db.String(100))
    rosca_martelo= db.Column(db.String(100), primary_key=False)
    agachamento = db.Column(db.String(100))
    legpress = db.Column(db.String(100))
    cadeira_extensora = db.Column(db.String(100), primary_key=False)
    cadeira_flexora = db.Column(db.String(100))
    panturrilhas = db.Column(db.String(100))
    cardio = db.Column(db.String(100))
    luta = db.Column(db.String(100), primary_key=False)
    fk_Cliente_id_cliente = db.Column(db.Integer)


    def __init__(self, id_ficha,data_criacao, descricao, duracao_treino, ombro_lateral,
                 ombro_frontal, supino_reto, supino_inclinado, crucifixo, puxador_frontal,
                 puxador_costas, remada_baixa, remada_cavalo, triceps_corda, triceps_pulley,
                 rosca_biceps, rosca_martelo, agachamento , legpress, cadeira_extensora,
                 cadeira_flexora, panturrilhas, cardio, luta, fk_Cliente_id_cliente):

        self.id_ficha =  id_ficha
        self.data_criacao = data_criacao
        self.descricao = descricao
        self.duracao_treino=duracao_treino
        self.ombro_lateral=ombro_lateral
        self.ombro_frontal=ombro_frontal
        self.supino_reto=supino_reto
        self.supino_inclinado=supino_inclinado
        self.crucifixo=crucifixo
        self.puxador_frontal=puxador_frontal
        self.puxador_costas=puxador_costas
        self.remada_baixa=remada_baixa
        self.remada_cavalo=remada_cavalo
        self.triceps_corda=triceps_corda
        self.triceps_pulley=triceps_pulley
        self.rosca_biceps=rosca_biceps
        self.rosca_martelo=rosca_martelo
        self.agachamento=agachamento
        self.legpress=legpress
        self.cadeira_extensora = cadeira_extensora
        self.cadeira_flexora=cadeira_flexora
        self.panturrilhas=panturrilhas
        self.cardio=cardio
        self.luta=luta
        self.fk_Cliente_id_cliente=fk_Cliente_id_cliente
