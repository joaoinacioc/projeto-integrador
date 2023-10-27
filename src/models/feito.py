from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Creating the Inserttable for inserting data into the database


class Feito(db.Model):
    '''Data for ON/OFF should be dumped in this table.'''

    __tablename__ = 'feito'
    fk_Instrutor_id_instrutor = db.Column(db.Integer, primary_key=True, nullable=False)
    fk_Ficha_de_Treino_id_ficha = db.Column(db.Integer, primary_key=True, nullable=False)


    def __init__(self, fk_Ficha_de_Treino_id_ficha, fk_Instrutor_id_instrutor ):
        self.fk_Instrutor_id_instrutor = fk_Instrutor_id_instrutor
        self.fk_Ficha_de_Treino_id_ficha =  fk_Ficha_de_Treino_id_ficha