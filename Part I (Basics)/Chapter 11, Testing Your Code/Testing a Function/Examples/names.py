from formatted_name_fucntion import get_formatted_name

print("Enter 'q' anytime to quit")
while True:
    first_name = input('\nEnter your first name: \n').strip()
    if first_name.lower().strip() == 'q':
        break

    second_name = input('\nEnter your second name: \n').strip()
    if second_name.lower().strip() == 'q':
        break
    formatted_name = get_formatted_name(first_name, second_name)

    print(f'\nYour formatted name is {formatted_name}')

print("You pressed 'q' so the program has ended. See you soon.")