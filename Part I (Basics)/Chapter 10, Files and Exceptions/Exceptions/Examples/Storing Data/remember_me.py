import json

username = input("\nWhat is your full name? \n").title().strip()
full_name = username.split()

try:
    first_name, username, surname = full_name[0], full_name[1], full_name[-1]

except IndexError:
    if len(full_name) == 2:
        first_name, username = full_name[0], full_name[1]

    elif len(full_name) == 1:
        username = full_name[0]

filename = 'username.json'
with open(filename, 'w') as f_obj:
    json.dump(full_name, f_obj)
    print(f"We'll remember your name next time you come back {username}. \n")
