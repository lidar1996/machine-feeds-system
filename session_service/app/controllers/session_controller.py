from flask import jsonify
from app.models.session import load_sessions_from_file
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG)

def get_sessions_by_machine_id(machine_id):
    """
    Returns a list of session related to the given machine_id in JSON format.
    """
    # Load sessions from the JSON file
    try:
        sessions = load_sessions_from_file()
        # Filter by machine ID
        machine_sessions = [session.to_dict() for session in sessions if session.machine_id == machine_id]
        return jsonify(machine_sessions)
    except Exception as e:
        logging.error(f"Error loading sessions: {e}")
        return jsonify({"error": str(e)}), 500