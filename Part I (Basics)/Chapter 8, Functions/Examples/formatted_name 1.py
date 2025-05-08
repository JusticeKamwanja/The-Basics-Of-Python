def get_formatted_name(first_name, second_name):
    """Return full name, neatly formatted"""
    full_name =f'{first_name} {second_name}.'
    return full_name.title()

person = get_formatted_name('justice', 'kamwanja')
print(f"\nThe person's name is {person} \n")