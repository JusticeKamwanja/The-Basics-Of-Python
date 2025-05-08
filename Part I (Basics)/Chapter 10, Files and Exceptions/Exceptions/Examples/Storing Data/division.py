from random import choice

print('\nGive me two numbers, and I will divide them.')
print(" Enter 'q' to quit.")

while True:
    first_number = float(input('\nFirst number: \n'))
    if first_number == 'q':
        print('Ok, bye.')
        break
    
    second_number = float(input('Second number.: \n'))
    if second_number == 'q':
        print('Ok, bye.')
        break


    try:
        answer = first_number / second_number

    except ZeroDivisionError:
        print(choice([
            'You cannot divide by zero.',
            'Why are you trying to divide by zero?',
            f"You can't divide {first_number} by zero.", 
            "You can't divide any number by zero.",
        ]))

    else:
        print(answer)