import json

def save_data(data, FILENAME):
    with open(FILENAME, 'w') as file:
        json.dump(data, file, indent=4)