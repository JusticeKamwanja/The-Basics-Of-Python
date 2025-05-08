# Start with a copy of your program from Exercise 8-9.
# Write a function called make_great() that modifies
# the list of magicians by adding the phrase the Great to each magician’s name.
# Call show_magicians() to see that the list has actually been modified.

magicians_list = ['chris angel', 'dynamo', 'carbonado']
magicians_list_2 = ['kamwanja', 'pearl', 'cynthia', 'faith']

def make_great(magicians):
    magician_number = 0
    for magician in magicians:
            magician = f'Great {magician}'
            print(f'The magician is called {magician.title()}.')

make_great(magicians_list)
print('\n')
make_great(magicians_list_2)