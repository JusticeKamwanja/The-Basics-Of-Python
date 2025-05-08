import json

def get_stored_name():
    """Get the stored name if available."""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            full_name = json.load(f_obj)

    except FileNotFoundError:
        return None
    
    else:
        return full_name
    
def get_new_username():
    """Prompt for a new username."""
    username = input("What is your full name?: \n").title().strip()
    full_name = username.split()
    # Choose which name to use.
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
    
    return full_name
    
def greet_user():
    """Greet the user by name."""
    full_name = get_stored_name()
    if full_name:
        print(f'Welcome back {full_name[0].title()}.')

    else:
        full_name = get_new_username()
        print(f"We'll remember you next time you come back {full_name[0]}.")

greet_user()