from flask import Blueprint
from controllers.machine_controller import index, insert, cliente

blueprint = Blueprint('blueprint', __name__)

blueprint.route('/', methods=['GET'])(index)
#blueprint.route('/create', methods=['GET'])(create)
blueprint.route('/insert', methods=['GET'])(insert)
blueprint.route('/cliente', methods=['GET'])(cliente)

