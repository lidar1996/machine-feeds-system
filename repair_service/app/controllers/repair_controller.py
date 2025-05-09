from flask import jsonify
from app.models.repair import load_repairs_from_file
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG)

def get_repairs_by_machine_id(machine_id):
    """
    Returns a list of repairs related to the given machine_id in JSON format.
    """
    # Load repairs from the JSON file
    try:
        repairs = load_repairs_from_file()
        # Filter by machine ID
        machine_repairs = [repair.to_dict() for repair in repairs if repair.machine_id == machine_id]
        return jsonify(machine_repairs)
    except Exception as e:
        logging.error(f"Error loading repairs: {e}")
        return jsonify({"error": str(e)}), 500