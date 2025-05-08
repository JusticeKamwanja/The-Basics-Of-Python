# Load the username, if it has been stored previously.
# Otherwise, prompt for the username and store it.
import json

"""Greet the user by name."""
filename = 'username.json'

try:
    with open(filename) as f_obj:
        full_name = json.load(f_obj)

except FileNotFoundError:
    username = input('What  is your name?; \n').title().strip()
    full_name = username.split()

    # Choose which name to use.
    try:
        first_name, username, surname = full_name[0], full_name[1], full_name[-1]

    except IndexError:
        if len(full_name) == 2:
            first_name, username = full_name[0], full_name[1]

        elif len(full_name) == 1:
            username = full_name[0]

    with open(filename, 'w') as f_obj:
        json.dump(full_name, f_obj)
        print(f"We'll remember you next time you come back {full_name[0]}.")

else:
    print(f'\nWelcome back {full_name[0].title()}. \n')