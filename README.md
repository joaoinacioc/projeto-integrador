# projeto-integrador
Repositorio de desenvolvimento de software para uma academia.

1 - ??

2 - O projeto consiste em uma plataforma de Academia que disponibiliza á equipe da academia criar a conta dos alunos, criar a ficha, e preenche-la com treinos, que o aluno que teve a conta criada possa logar no sistema e visualizar o treino que foi passado.

3 - O programa tem várias funções testáveis, uma delas é o próprio login do usuário, que busca no banco de dados o email e senha, e retorna algo de certa maneira dependendo do resultado do login (se deu certo, ou as credenciais estavam erradas ou não), por exemplo no codigo:

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