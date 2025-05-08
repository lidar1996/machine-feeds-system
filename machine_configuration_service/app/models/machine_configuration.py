import json
from pathlib import Path

class MachineConfiguration:
    def __init__(self, id, created_at, data):
        self.id = id
        self.created_at = created_at
        self.data = data

    def to_dict(self):
        return {
            "id": self.id,
            "created_at": self.created_at,
            "data": self.data
        }

def load_machine_configuration_from_file():
    """
    Load machine configuration from a JSON file.
    """
    file_path = Path(__file__).parent.parent / "data/machine_configurations_data.json"
    with open(file_path, 'r') as file:
        data = json.load(file)
        return [MachineConfiguration(**item) for item in data]