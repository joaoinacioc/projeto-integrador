import json
from models.cliente import Cliente
from models.plano_mensal import PlanoMensal
from models.forma_pagamento import FormaPagamento
from models.ficha_treino import Ficha_Treino
from models.instrutor import  Instrutor
from src.config import db

from models.feito import Feito
#def create_logic():
    #try:
        # create tables if not exists.
        #db.create_all()
        #db.session.commit()
        #return '==================TABLES CREATED=================='

    #except Exception as e:
        #print(e)
        #return '==================TABLES NOT CREATED!!!=================='


def insert_logic():
    data = json.load(open("data.json", 'r'))


    cliente = Cliente(nome=data['nome'], sobrenome=data['sobrenome'], cpf=data['cpf'],
                      data_nascimento=data['data_nascimento'], email=data['email'], senha=data['senha'], telefone=data['telefone'])


    forma_pagamento = FormaPagamento(id_forma_pagamento=data['id_forma_pagamento'],
                                     tipo_pagamento=data['tipo_pagamento'],
                                     fk_plano_mensal_id_plano=data['fk_plano_mensal_idplano']
                                     )

    plano_mensal = PlanoMensal(id_plano=data['id_plano'], nome=data['nome'],
                                descricao=data['descricao'], preco=data['preco']
                               )
    ficha_treino = Ficha_Treino(id_ficha=data['id_ficha'], data_criacao=data['data_criacao'],
                                descricao=data['descricao'], duracao_treino=data['duracao_treino'],
                                ombro_lateral=data['ombro_lateral'],ombro_frontal=data['ombro_frontal'],
                                supino_reto = data['supino_reto'], supino_inclinado=data['supino_inclinado'],
                                crucifixo=data['crucifixo'], puxador_frontal=data['puxador_frontal'],
                                puxador_costas=data['puxador_costas'], remada_baixa=data['remada_baixa'],
                                remada_cavalo=data['remada_cavalo'], triceps_corda=data['triceps_corda'],
                                triceps_pulley=data['triceps_pulley'],rosca_biceps=data['rosca_biceps'],
                                rosca_martelo=data['rosca_martelo'], agachamento=data['agachamento'],
                                legpress=data['legpress'],cadeira_extensora=data['cadeira_extensora'],
                                cadeira_flexora=data['cadeira_flexora'], panturrilhas=data['panturrilhas'],
                                cardio=data['cardio'], luta=data['luta'],
                                fk_Cliente_id_cliente=data['fk_Cliente_id_cliente'])

    instrutor = Instrutor(id_instrutor=data['id_instrutor'], nome=data['nome'],
                          cpf=data['cpf'], data_nascimento=data['data_nascimento'],
                          email=data['email'], senha=data['senha'], telefone=data['telefone']
                          )
    #feito = Feito(fk_Ficha_de_Treino_id_ficha=data['fk_Ficha_de_Treino_id_ficha'],
                  #fk_Instrutor_id_instrutor=data['fk_Instrutor_id_instrutor']
                  #)


    db.session.add(cliente, forma_pagamento, plano_mensal, ficha_treino, instrutor)
    db.session.commit()
    db.session.close()
    return '==================DATA INSERTED=================='

from models.cliente import Cliente  # Importe o modelo Cliente

def login_logic(email, senha):
    # Consulte o banco de dados para verificar as credenciais
    cliente = Cliente.query.filter_by(email=email, senha=senha).first()

    # Se o cliente existir, as credenciais são válidas
    return cliente is not None

