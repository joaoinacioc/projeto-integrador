from flask import Blueprint

from controllers.machine_controller import index, alterar_plano,insert,excluir_conta,confirmar_exclusao_conta, logout_cliente, atualizar_ficha_treino, cliente, login_cliente, login_instrutor, cadastro, processar_cadastro, logar_cliente, alterar_plano, ficha_treino, instrutor
blueprint = Blueprint('blueprint', __name__)
blueprint.route('/', methods=['GET'])(index)
#blueprint.route('/create', methods=['GET'])(create)
blueprint.route('/insert', methods=['GET'])(insert)
blueprint.route('/cliente', methods=['GET'])(cliente)
blueprint.route('/login', methods=['GET'])(login_cliente)
blueprint.route('/logar-instrutor', methods=['POST'])(login_instrutor)
blueprint.route('/login-instrutor', methods=['GET', 'POST'])(instrutor)
blueprint.route('/instrutor', methods=['GET', 'POST'])(instrutor)
blueprint.route('/cadastro', methods=['GET'])(cadastro)
blueprint.route('/cadastro', methods=['POST'])(processar_cadastro)
blueprint.route('/logar_cliente', methods=['POST'])(logar_cliente)
blueprint.route('/alterar-plano', methods=['POST'])(alterar_plano)
blueprint.route('/ficha_treino', methods=['GET', 'POST'])(ficha_treino)
blueprint.route('/atualizar-ficha-treino', methods=['POST'])(atualizar_ficha_treino)
blueprint.route('/logout-cliente')(logout_cliente)
blueprint.route('/confirmar_exclusao_conta')(confirmar_exclusao_conta)
blueprint.route('/excluir_conta', methods=['GET'])(excluir_conta)
blueprint.route('/trocar_plano', methods=['GET'])(alterar_plano)

