import requests

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
        return {}

def get_repairs(machine_id):
    """
    Fetch repairs for a given machine ID.
    """
    try:
        res = requests.get(f"{REPAIR_URL}/{machine_id}")
        return res.json()
    except Exception:
        return []

def get_sessions(machine_id):
    """
    Fetch sessions for a given machine ID.
    """
    try:
        res = requests.get(f"{SESSION_URL}/{machine_id}")
        return res.json()
    except Exception:
        return []
