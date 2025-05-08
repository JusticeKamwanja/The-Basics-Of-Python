def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f'{first_name} {last_name}'
    return full_name.title()

# This is an infinite loop!
while True:
    print('\nPlease enter your name.')
    print("(Enter 'q' any time to quit) \n")

    f_name = input('First name.: \n').strip()
    if f_name.lower() == 'q':
        break

    l_name = input('Last name.: \n').strip()
    if l_name.lower() == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f'\nHello {formatted_name.title()}!')

print("\nAlright, We're done here.")