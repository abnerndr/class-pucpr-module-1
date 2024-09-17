import os
import json

def load_data(FILENAME):
    # verifica se o arquivo existe pela lib os e traz os dados dele
    if os.path.exists(FILENAME):
        with open(FILENAME, 'r') as file:
            return json.load(file)
    return []