from flask import Blueprint
from ..controllers.machine_feeds_controller import fetch_combined_feeds

machine_feeds_bp = Blueprint('machine_feeds', __name__)

@machine_feeds_bp.route('/machine-feeds/<string:machine_id>', methods=['GET'])
def combined_feeds(machine_id):
    """
    Route to fetch combined feeds for a given machine ID.
    """
    return fetch_combined_feeds(machine_id)