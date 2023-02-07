import json
class config:
    def __init__(self) -> None:
        pass
    
    def read_config():
        json_file = open('config\config.json')
        data = json.load(json_file)
        return data