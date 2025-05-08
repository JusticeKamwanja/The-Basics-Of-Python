def make_pizza(size, *toppings):
    print(f'\nMaking a {size}-inch pizza with the following:')

    number = 0
    for topping in toppings:
        number += 1
        print(f'{number}. {topping.title()}')

    print('\nFinished amaking your pizza!! \n')

make_pizza(16, 'pepperoni')
make_pizza(20, 'green peppers', 'pineapple', 'mushrooms', 'pepperoni')