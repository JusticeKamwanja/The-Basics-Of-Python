# Make a list of magician’s names.
# Pass the list to a function called show_magicians(),
# which prints the name of each magician in the list.

magicians_list = ['chris angel', 'dynamo', 'carbonado']
magicians_list_2 = ['kamwanja', 'pearl', 'cynthia', 'faith']

def show_magicians(magicians):
    magician_number = 0
    for magician in magicians:
            print(f'The magician is called {magician.title()}.')

show_magicians(magicians_list)
print('\n')
show_magicians(magicians_list_2)
