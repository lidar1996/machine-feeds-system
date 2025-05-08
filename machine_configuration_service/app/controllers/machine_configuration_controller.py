from flask import jsonify
from machine_configuration_service.app.models.machine_configuration import load_machine_configuration_from_file

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
    return jsonify({"error": "Machine Configuration not found"}), 404