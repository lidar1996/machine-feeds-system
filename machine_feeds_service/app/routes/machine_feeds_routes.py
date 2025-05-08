from flask import Blueprint
from machine_feeds_service.app.controllers.machine_feeds_controller import fetch_combined_feeds

machine_feeds_bp = Blueprint('machine_feeds', __name__)

@machine_feeds_bp.route('/machine_feeds/<string:machine_id>', methods=['GET'])
def combined_feeds(machine_id):
    """
    Route to fetch combined feeds for a given machine ID.
    """
    return fetch_combined_feeds(machine_id)