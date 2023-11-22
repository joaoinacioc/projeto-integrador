import json
from flask import request, redirect, url_for, Flask, render_template, session
from flask_sqlalchemy import SQLAlchemy
from services.user_service import insert_logic, Cliente, login_logic
from src.config import db
from models.ficha_treino import Ficha_Treino
from models.instrutor import Instrutor
from datetime import datetime
from flask import redirect, url_for, flash


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
            mensagem_erro = 'Credenciais inválidas. Tente novamente.'
            return render_template('login.html', mensagem_erro=mensagem_erro)

    # Adicione um retorno padrão para casos em que o método não seja POST
    return "Método não permitido"

def instrutor():
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
        fk_Plano_Mensal_id_plano=fk_Plano_Mensal_id_plano
    )

    db.session.add(novo_cliente)
    db.session.commit()

    # Agora, você pode obter o id_cliente do novo cliente
    id_cliente = novo_cliente.id_cliente

    # Chamar a função criar_ficha_treino com o id_cliente
    criar_ficha_treino(id_cliente)

    # Redirecione o usuário para uma página de confirmação ou outra página
    return render_template('login.html')


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

                return redirect(url_for('blueprint.cliente'))
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

        nome_cliente = cliente.nome if cliente else "Cliente"
        # Verifica se o cliente existe
        if cliente:
            # Substitua a linha abaixo pela lógica real para obter a ficha de treino
            ficha_treino = Ficha_Treino.query.filter_by(fk_Cliente_id_cliente=cliente_id).first()

            # Renderiza a página com a ficha de treino
            return render_template('ficha-treino.html', ficha_treino=ficha_treino)

    # Se o ID do cliente não estiver na sessão, redirecione para a página de login
    return redirect(url_for('blueprint.login_cliente'))
def cliente():
    # Verifica se o ID do cliente está na sessão
    if 'cliente_id' in session:
        # Obtém o ID do cliente da sessão
        cliente_id = session['cliente_id']

        # Consulta o banco de dados para obter o cliente pelo ID
        cliente = Cliente.query.get(cliente_id)

        # Verifica se o cliente existe
        if cliente:
            # Renderiza a página do cliente, passando a variável cliente para o template
            return render_template('cliente.html', cliente=cliente)

    # Se o ID do cliente não estiver na sessão, redirecione para a página de login
    return redirect(url_for('blueprint.login_cliente'))



def login_instrutor():
    # Lógica para verificar as credenciais do instrutor
    email = request.form.get('email')
    senha = request.form.get('senha')
    instrutor = Instrutor.query.filter_by(email=email, senha=senha).first()

    # Lógica para verificar as credenciais (substitua por sua própria lógica)
    if instrutor:
        # Se o instrutor existe, armazenar o ID na sessão ou outra lógica desejada
        # session['instrutor_id'] = instrutor.id_instrutor
        return redirect(url_for('blueprint.instrutor'))  # Substitua 'instrutor' pelo nome da sua rota protegida
    else:
        # Se as credenciais forem inválidas, exiba uma mensagem de erro
        flash('Credenciais inválidas. Tente novamente.', 'erro')

    # Se a solicitação for POST ou as credenciais forem inválidas, renderize a página de login
    return render_template('login-instrutor.html')
def atualizar_ficha_treino():
    if request.method == 'POST':
        # Obter os dados do formulário
        descricao = request.form.get('descricao')
        duracao_treino = request.form.get('duracao_treino')
        ombro_lateral = request.form.get('ombro_lateral')
        ombro_frontal = request.form.get('ombro_frontal')
        supino_reto = request.form.get('supino_reto')
        supino_inclinado = request.form.get('supino_inclinado')
        crucifixo = request.form.get('crucifixo')
        puxador_frontal = request.form.get('puxador_frontal')
        puxador_costas = request.form.get('puxador_costas')
        remada_baixa = request.form.get('remada_baixa')
        remada_cavalo = request.form.get('remada_cavalo')
        triceps_corda = request.form.get('triceps_corda')
        triceps_pulley = request.form.get('triceps_pulley')
        rosca_biceps = request.form.get('rosca_biceps')
        rosca_martelo = request.form.get('rosca_martelo')
        agachamento = request.form.get('agachamento')
        legpress = request.form.get('legpress')
        cadeira_extensora = request.form.get('cadeira_extensora')
        cadeira_flexora = request.form.get('cadeira_flexora')
        panturrilhas = request.form.get('panturrilhas')
        cardio = request.form.get('cardio')
        fitdance = request.form.get('fitdance')
        luta = request.form.get('luta')

        # Atualizar os dados no banco de dados
        ficha_treino = Ficha_Treino.query.filter_by(fk_Cliente_id_cliente=session['cliente_id']).first()
        if ficha_treino:
            ficha_treino.descricao = descricao
            ficha_treino.duracao_treino = duracao_treino
            ficha_treino.ombro_lateral = ombro_lateral
            ficha_treino.ombro_frontal = ombro_frontal
            ficha_treino.supino_reto = supino_reto
            ficha_treino.supino_inclinado = supino_inclinado
            ficha_treino.crucifixo = crucifixo
            ficha_treino.puxador_frontal = puxador_frontal
            ficha_treino.puxador_costas = puxador_costas
            ficha_treino.remada_baixa = remada_baixa
            ficha_treino.remada_cavalo = remada_cavalo
            ficha_treino.triceps_corda = triceps_corda
            ficha_treino.triceps_pulley = triceps_pulley
            ficha_treino.rosca_biceps = rosca_biceps
            ficha_treino.rosca_martelo = rosca_martelo
            ficha_treino.agachamento = agachamento
            ficha_treino.legpress = legpress
            ficha_treino.cadeira_extensora = cadeira_extensora
            ficha_treino.cadeira_flexora = cadeira_flexora
            ficha_treino.panturrilhas = panturrilhas
            ficha_treino.cardio = cardio
            ficha_treino.fitdance = fitdance
            ficha_treino.luta = luta

            # Atualize os outros campos conforme necessário
            db.session.commit()

        # Redirecionar para a página da ficha de treino ou outra página desejada
        return redirect(url_for('blueprint.ficha_treino'))

def criar_ficha_treino(id_cliente):

    nova_ficha_treino = Ficha_Treino(
        data_criacao=datetime.utcnow(),
        descricao='-',
        duracao_treino='-',
        ombro_lateral='-',
        ombro_frontal='-',
        supino_reto='-',
        supino_inclinado='-',
        crucifixo='-',
        puxador_frontal='-',
        puxador_costas='-',
        remada_baixa='-',
        remada_cavalo='-',
        triceps_corda='-',
        triceps_pulley='-',
        rosca_biceps='-',
        rosca_martelo='-',
        agachamento='-',
        legpress='-',
        cadeira_extensora='-',
        cadeira_flexora='-',
        panturrilhas='-',
        cardio='-',
        fitdance='-',
        luta='-',
        fk_Cliente_id_cliente=id_cliente)
    db.session.add(nova_ficha_treino)
    db.session.commit()

def instrutor_logado():
    return render_template('instrutor.html')

def logout_cliente():
    # Remover a chave associada à sessão do cliente
    session.pop('cliente_id', None)
    # Redirecionar para a página de login ou outra página desejada
    return redirect(url_for('blueprint.index'))

def confirmar_exclusao_conta():
    # Renderizar a página de confirmação de exclusão da conta
    return render_template('confirmar_exclusao.html')

def excluir_conta():
    # Obter o ID do cliente da sessão
    cliente_id = session.get('cliente_id')

    # Verificar se o ID do cliente está presente
    if cliente_id:
        # Obter o cliente pelo ID
        cliente = Cliente.query.get(cliente_id)

        # Verificar se o cliente existe
        if cliente:
            # Excluir o cliente do banco de dados
            db.session.delete(cliente)
            db.session.commit()

            # Limpar a sessão do cliente
            session.pop('cliente_id', None)

            # Redirecionar para a página de login ou outra página desejada
            return redirect(url_for('blueprint.login_cliente'))

    # Se não houver ID de cliente na sessão ou se ocorrer um problema, redirecionar para a página do cliente
    return redirect(url_for('blueprint.cliente'))