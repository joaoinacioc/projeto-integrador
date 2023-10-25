from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Creating the Inserttable for inserting data into the database


class FormaPagamento(db.Model):
    '''Data for ON/OFF should be dumped in this table.'''

    __tablename__ = 'forma_pagamento'
    id_forma_pagamento = db.Column(db.Integer, primary_key=True)
    tipo_pagamento = db.Column(db.String(50), nullable=False)
    fk_plano_mensal_id_plano = db.Column(db.Integer, nullable=False)

    # method used to represent a class's objects as a string
    def __init__(self, id_forma_pagamento, tipo_pagamento, fk_plano_mensal_id_plano):
        self.id_forma_pagamento = id_forma_pagamento
        self.tipo_pagamento = tipo_pagamento
        self.fk_PlanoMensal_id_plano = fk_plano_mensal_id_plano
