import requests
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG)

REPAIR_URL = "http://repair_service:5002/repairs"
SESSION_URL = "http://session_service:5003/sessions"
MACHINE_CONFIGURATION_URL = "http://machine_configuration_service:5001/machine_configurations"

def get_machine_configuration(machine_id):
    """
    Fetch machine configuration for a given machine ID.
    """
    try:
        res = requests.get(f"{MACHINE_CONFIGURATION_URL}/{machine_id}")
        return res.json()
    except Exception:
        logging.error(f"Error fetching machine configuration for ID {machine_id}")
        return {}

def get_repairs(machine_id):
    """
    Fetch repairs for a given machine ID.
    """
    try:
        res = requests.get(f"{REPAIR_URL}/{machine_id}")
        return res.json()
    except Exception:
        logging.error(f"Error fetching repairs for ID {machine_id}")
        return []

def get_sessions(machine_id):
    """
    Fetch sessions for a given machine ID.
    """
    try:
        res = requests.get(f"{SESSION_URL}/{machine_id}")
        return res.json()
    except Exception:
        logging.error(f"Error fetching sessions for ID {machine_id}")
        return []
