# Start with your work from Exercise 8-10.
# Call the function make_great() with a copy of the list of magicians’ names.
# Because the original list will be unchanged, return the new list and store it in a separate list.
# Call show_magicians() with each list to show that you have one list of the original names
# and one list with the Great added to each magician’s name.


magicians_list = ['chris angel', 'dynamo', 'carbonado']
magicians_list_2 = ['kamwanja', 'pearl', 'cynthia', 'faith']

def make_great(magicians):
    magician_number = 0
    for magician in magicians:
        magician = f'Great {magician}'
        print(f'The magician is called {magician.title()}.')
    
    return magicians[:]

make_great(magicians_list)
magicians_list.append('michael')
print('\n')
make_great(magicians_list)