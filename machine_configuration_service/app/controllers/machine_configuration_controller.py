from flask import jsonify
from ..models.machine_configuration import load_machine_configuration_from_file
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG)

def get_machine_configuration_by_id(machine_id):
    """
    Get machine configuration by ID.
    """
    # Load machine configurations from the JSON file
    machine_configurations = load_machine_configuration_from_file()
    # Filter the machine configuration by ID
    for machine_configuration in machine_configurations:
        if machine_configuration.id == machine_id:
            return jsonify(machine_configuration.to_dict())
    logging.error(f"Machine Configuration with ID {machine_id} not found")
    return jsonify({"error": "Machine Configuration not found"}), 404