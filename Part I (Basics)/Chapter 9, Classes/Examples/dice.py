# Make a class Die with one attribute called sides, which has a default value of 6.
# Write a method called roll_die() that prints a random number # between 1 and the number of sides the die has.
# Make a 6-sided die and roll it 10 times.
# Make a 10-sided die and a 20-sided die. Roll each die 10 times

from random import randint

class Die():
    def __init__(self, sides):
        self.sides = sides

    def roll_die(self, roll_count):
        print(f'Rolling die.')
        for roll in range(1, roll_count+1): # For every roll,
            number = randint(1, self.sides) # generate a random number,
            print(f' {number}') # then print it.
        print('\n')
    
        
die_1 = Die(6)
die_2 = Die(10)
die_3 = Die(20)


die_1.roll_die(10)
die_2.roll_die(10)
die_3.roll_die(10)