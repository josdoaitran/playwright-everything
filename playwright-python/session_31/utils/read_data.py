import json
import yaml

def read_json_by_key(file_path, key):
    with open(file_path) as user_file:
        file_contents = user_file.read()
    parsed_json = json.loads(file_contents)
    return parsed_json[key]


def read_yml_by_key(file_path, key):
    with open(file_path, 'r') as f:
        data = yaml.full_load(f)
        value = data.get(key)
        return value


