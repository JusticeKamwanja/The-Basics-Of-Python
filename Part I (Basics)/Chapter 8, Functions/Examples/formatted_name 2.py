def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = f'{first_name} {middle_name} {last_name}'
    else:
        full_name = f'{first_name} {last_name}'

    return full_name.title()

name_1 = input('Enter your first name.: \n')
name_mid = input('Enter your middle name. \n(if you dont have one, press enter): \n')
name_2 = input('Enter your last name.: \n')

person = get_formatted_name(first_name = name_1, middle_name = name_mid, last_name = name_2)

print(f'\nYour full name is {person}.')
