import json
from flask import request, redirect, url_for, Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from services.user_service import insert_logic, Cliente
from src.config import db
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

    # Criar um novo registro de cliente no banco de dados
    novo_cliente = Cliente(
        nome=nome,
        sobrenome=sobrenome,
        cpf=cpf,
        data_nascimento=data_nascimento,
        email=email,
        senha=senha,
        telefone=telefone,
    )

    db.session.add(novo_cliente)
    db.session.commit()

    # Redirecione o usuário para uma página de confirmação ou outra página
    return "Cadastro realizado com sucesso!"
