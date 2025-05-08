import json
from pathlib import Path

class Repair:
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

def load_repairs_from_file():
    """
    Load repairs from a JSON file.
    """
    file_path = Path(__file__).parent.parent / "data/repairs_data.json"
    with open(file_path, 'r') as file:
        data = json.load(file)
        return [Repair(**item) for item in data]