from flask import jsonify
from ..services.external_api import get_repairs, get_sessions, get_machine_configuration

def fetch_combined_feeds(machine_id):
    """
    Fetch combined feeds for a given machine ID.
    """
    machine_configuration = get_machine_configuration(machine_id)
    if not machine_configuration or "error" in machine_configuration:
        return jsonify({"error": machine_configuration.get("error", "Machine configuration not found")}), 404

    repairs = get_repairs(machine_id)
    sessions = get_sessions(machine_id)

    for r in repairs:
        r['type'] = 'repair'
    for s in sessions:
        s['type'] = 'session'

    combined = repairs + sessions
    combined.sort(key=lambda x: x['created_at'], reverse=True)
    return jsonify({
        "machine_configuration": machine_configuration, "activities": combined
    }), 200
