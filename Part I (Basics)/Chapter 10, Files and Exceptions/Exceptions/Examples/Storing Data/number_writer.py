import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'number_list.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)