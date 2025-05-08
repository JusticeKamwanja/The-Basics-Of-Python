# Make a class called User.

# Create two attributes called first_name and last_name,

# and then create several other attributes that are typically stored in a user profile.

# Make a method called describe_user() that prints a summary of the user’s information.

# Make another method called greet_user() that prints a personalized greeting to the user.

# Create several instances representing different users, and call both methods for each user.

class User():
    def __init__(self, age, first_name, last_name, middle_name='', hometown=''):
        
        self.age = age
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.hometown = hometown

    def describe_user(self):
        print(f'\nHere is some information about the user:')
        print(f'The user is called {self.first_name.title()} {str(self.middle_name.title())} {self.last_name.title()}.')
        if self.hometown:
            print(f'{self.first_name.title()} is a {self.age} year old from {self.hometown.title()}. \n')

        else:
            print(f'{self.first_name.title()} is a {self.age} year old. \n')
        
me = User(22, 'justice', 'kamwanja', hometown='eldoret')
mayson = User(25, 'Mayson', 'Kimutai')
pearl = User(24, 'pearl', 'cheshari', middle_name='momo temko')

mayson.describe_user()
pearl.describe_user()
me.describe_user()

