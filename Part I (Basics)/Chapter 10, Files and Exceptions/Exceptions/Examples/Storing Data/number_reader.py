import json

filename = 'number_list.json'

with open(filename) as num:
    info = json.load(num)
    print(f'The information stored is as follows: \n{info} \n')