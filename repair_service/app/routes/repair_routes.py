from flask import Blueprint
from ..controllers.repair_controller import get_repairs_by_machine_id

repair_bp = Blueprint('repair', __name__)

@repair_bp.route('/repairs/<string:machine_id>', methods=['GET'])
def repairs_by_machine_id(machine_id):
    """
    Route to get repairs by machine ID.
    """
    return get_repairs_by_machine_id(machine_id)