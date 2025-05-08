from flask import Blueprint
from app.controllers.machine_configuration_controller import get_machine_configuration_by_id

machine_configuration_bp = Blueprint('machine_configuration', __name__)

@machine_configuration_bp.route('/machine_configurations/<string:machine_id>', methods=['GET'])
def machine_configuration_by_id(machine_id):
    """
    Route to get machine configuration by ID.
    """
    return get_machine_configuration_by_id(machine_id)