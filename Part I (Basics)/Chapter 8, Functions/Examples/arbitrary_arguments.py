def make_pizza(*toppings):
    """Print a list of the requested toppings."""
    for topping in toppings:
        print(f'Adding {topping}...')
        
    print('\nYour pizza is done!! \n')

make_pizza('mushrooms', 'pineapple', 'green peppers', 'pepperoni')

make_pizza('pineapple', 'bell pepper')

make_pizza('pineapple', 'green peppers', 'onion.')
