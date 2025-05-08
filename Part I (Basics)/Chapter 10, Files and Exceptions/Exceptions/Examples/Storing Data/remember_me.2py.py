import json

filename = 'username.json'

with open(filename) as f_obj:
    full_name = json.load(f_obj)
    print(f'\nWelcome back {full_name[0]}!!! \n')