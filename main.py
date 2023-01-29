import json
from json.decoder import JSONDecodeError
import re

input_file = './data/data_1.json'
output_file = './schema/schema_1.json'

# Uncomment this line below to run the second json file
# input_file = './data/data_2.json'
# output_file = './schema/schema_2.json'

# Read JSON file
try:
    with open(input_file, 'r') as f:
        data = json.load(f)

    # Extract the 'message' key from the input data
    if "message" in data:
        data = data['message']

except FileNotFoundError as e:
    print(f'File not found: {e}')
    exit()
except KeyError as e:
    print(f'Key not found in JSON: {e}')
    exit()
except JSONDecodeError as e:
    print(f'Error reading JSON file: {e}')
    exit()


def add_keys(data, tag='', description='', required=False):
    if isinstance(data, dict):
        for key in data:
            if key == 'message':
                data[key] = add_keys(data[key], key, '', required)
            else:
                data[key] = add_keys(data[key], key, '', required)
    elif isinstance(data, list):
        for i in range(len(data)):
            if isinstance(data[i], str) and re.match("^[A-Z_]*$", data[i]):
                data = {'tag': tag, 'description': description,
                        'required': required, 'type': 'ENUM', 'value': data}
                break
            elif isinstance(data[i], dict) or isinstance(data[i], list):
                data[i] = add_keys(data[i], tag, description, required)
                data = {'tag': tag, 'description': description,
                        'required': required, 'type': 'ARRAY', 'value': data}
                break
            elif isinstance(data[i], int):
                data = {'tag': tag, 'description': description,
                        'required': required, 'type': 'INTEGER', 'value': data}
                break
            elif isinstance(data[i], str):
                data = {'tag': tag, 'description': description,
                        'required': required, 'type': 'STRING', 'value': data}
                break
    elif isinstance(data, int):
        data = {'tag': tag, 'description': description,
                'required': required, 'type': 'INTEGER', 'value': data}
    elif isinstance(data, str):
        data = {'tag': tag, 'description': description,
                'required': required, 'type': 'STRING', 'value': data}
    return data


schema = add_keys(data)

# Dump output to new file
try:
    with open(output_file, 'w') as f:
        json.dump(schema, f, indent=4)
    print(f'Schema written to {output_file}')
except JSONDecodeError as e:
    print(f'Error writing JSON file: {e}')
