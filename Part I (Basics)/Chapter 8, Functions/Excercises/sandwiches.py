# Write a function that accepts a list of items a person wants on a sandwich.
# The function should have one parameter that collects as many items as the function call provides,
# and it should print a summary of the sandwich that is being ordered.
# Call the function three times, using a different number of arguments each time.

def sandwich(*toppings):
    requested_toppings = []
    for topping in toppings:
        requested_toppings.append(topping)

    if len(requested_toppings) == 1:
        print('\nThe sandwich has the following topping:')
    else:
        print('\nThe sandwich has the following toppings:')
    for topping in requested_toppings:
        print(f'-{topping}')

sandwich('ham')
sandwich('ham', 'lettuce')
sandwich('ham', 'lettuce', 'tomatoes')