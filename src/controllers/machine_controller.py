import json
from flask import request, redirect, url_for, Flask, render_template, session
from flask_sqlalchemy import SQLAlchemy
from services.user_service import insert_logic, Cliente, login_logic
from src.config import db
from models.ficha_treino import Ficha_Treino

def index():
    return render_template('home.html')

#def create():

def cliente():
    return render_template('cliente.html')
#    create_logic()

# insert data into table.
def insert():
    insert_logic()

def login_cliente():
    return render_template('login.html')


def logar_cliente():
    if request.method == 'POST':
        # Obter os dados do formulário do objeto request
        email = request.form['email']
        senha = request.form['senha']

        # Consulte o banco de dados para verificar as credenciais
        cliente = Cliente.query.filter_by(email=email, senha=senha).first()

        if cliente:
            # Se o cliente existe, armazenar o ID na sessão
            session['cliente_id'] = cliente.id_cliente  # Ajuste aqui para 'id_cliente'
            return redirect(url_for('blueprint.cliente'))
        else:
            return "Credenciais inválidas. Tente novamente."

    # Adicione um retorno padrão para casos em que o método não seja POST
    return "Método não permitido"

def login_estrutor():
    return render_template('login-instrutor.html')

def cadastro():
    return render_template('cadastro.html')

def processar_cadastro():
    # Obter os dados do formulário do objeto request
    nome = request.form['nome']
    sobrenome = request.form['sobrenome']
    cpf = request.form['cpf']
    data_nascimento = request.form['data_nascimento']
    email = request.form['email']
    senha = request.form['senha']
    telefone = request.form['telefone']
    fk_Plano_Mensal_id_plano = request.form['plano_mensal']
    # Criar um novo registro de cliente no banco de dados
    novo_cliente = Cliente(
        nome=nome,
        sobrenome=sobrenome,
        cpf=cpf,
        data_nascimento=data_nascimento,
        email=email,
        senha=senha,
        telefone=telefone,
        fk_Plano_Mensal_id_plano = fk_Plano_Mensal_id_plano
    )

    db.session.add(novo_cliente)
    db.session.commit()

    # Redirecione o usuário para uma página de confirmação ou outra página
    return "Cadastro realizado com sucesso!"


def alterar_plano():
    if request.method == 'POST':
        # Verificar se o usuário está autenticado (tem um ID de cliente na sessão)
        if 'cliente_id' in session:
            cliente_id = session['cliente_id']

            # Obter o cliente do banco de dados usando o ID armazenado na sessão
            cliente = Cliente.query.get(cliente_id)

            if cliente:
                # Obter o novo plano do formulário
                novo_plano = request.form['plano_mensal']

                # Adicionar lógica para atualizar o plano no banco de dados
                cliente.plano_mensal = novo_plano
                db.session.commit()

                return "Plano alterado com sucesso!"
            else:
                return "Cliente não encontrado."
        else:
            return "Usuário não autenticado. Faça o login primeiro."

    # Adicione um retorno padrão para casos em que o método não seja POST
    return "Método não permitido"

def ficha_treino():
    # Verifica se o ID do cliente está na sessão
    if 'cliente_id' in session:
        # Obtém o ID do cliente da sessão
        cliente_id = session['cliente_id']

        # Consulta o banco de dados para obter o cliente pelo ID
        cliente = Cliente.query.get(cliente_id)

        # Verifica se o cliente existe
        if cliente:
            # Substitua a linha abaixo pela lógica real para obter a ficha de treino
            ficha_treino = Ficha_Treino.query.filter_by(fk_Cliente_id_cliente=cliente_id).first()

            # Renderiza a página com a ficha de treino
            return render_template('ficha-treino.html', ficha_treino=ficha_treino)

    # Se o ID do cliente não estiver na sessão, redirecione para a página de login
    return redirect(url_for('blueprint.login_cliente'))