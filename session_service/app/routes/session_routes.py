from flask import Blueprint
from session_service.app.controllers.session_controller import get_sessions_by_machine_id

session_bp = Blueprint('session', __name__)

@session_bp.route('/sessions/<string:machine_id>', methods=['GET'])
def sessions_by_machine_id(machine_id):
    """
    Route to get sessions by machine ID.
    """
    return get_sessions_by_machine_id(machine_id)