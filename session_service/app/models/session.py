import json
from pathlib import Path

class Session:
    def __init__(self, id, machine_id, created_at, data):
        self.id = id
        self.machine_id = machine_id
        self.created_at = created_at
        self.data = data

    def to_dict(self):
        return {
            "id": self.id,
            "machine_id": self.machine_id,
            "created_at": self.created_at,
            "data": self.data
        }

def load_sessions_from_file():
    """
    Load sessions from a JSON file.
    """
    file_path = Path(__file__).parent.parent / "data/sessions_data.json"
    with open(file_path, 'r') as file:
        data = json.load(file)
        return [Session(**item) for item in data]