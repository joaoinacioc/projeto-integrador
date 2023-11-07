from flask import Blueprint

from controllers.machine_controller import index, insert, cliente, login_cliente, login_estrutor, cadastro, processar_cadastro
blueprint = Blueprint('blueprint', __name__)
blueprint.route('/', methods=['GET'])(index)
#blueprint.route('/create', methods=['GET'])(create)
blueprint.route('/insert', methods=['GET'])(insert)
blueprint.route('/cliente', methods=['GET'])(cliente)
blueprint.route('/login', methods=['GET'])(login_cliente)
blueprint.route('/login-instrutor', methods=['GET'])(login_estrutor)
blueprint.route('/cadastro', methods=['GET'])(cadastro)
blueprint.route('/cadastro', methods=['POST'])(processar_cadastro)

