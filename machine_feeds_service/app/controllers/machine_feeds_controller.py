from flask import jsonify
import redis
import json
from ..services.external_api import get_repairs, get_sessions, get_machine_configuration

# Define Redis client
redis_client = redis.Redis(host='redis', port=6379, decode_responses=True)
CACHE_TTL_SECONDS = 300 # 5 minutes

def fetch_combined_feeds(machine_id):
    """
    Fetch combined feeds for a given machine ID.
    """
    # Check if the data is in the cache
    cache_key = f"machine_feeds:{machine_id}"
    cached_data = redis_client.get(cache_key)
    if cached_data:
        return jsonify(json.loads(cached_data)), 200

    # If not cached, fetch from external API
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
    result = {
        "machine_configuration": machine_configuration,
        "activities": combined
    }
    redis_client.setex(cache_key, CACHE_TTL_SECONDS, json.dumps(result))
    return jsonify(result), 200
