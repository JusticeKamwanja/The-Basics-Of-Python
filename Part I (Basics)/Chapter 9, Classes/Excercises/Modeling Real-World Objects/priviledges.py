# Write a separate Privileges class.
# The class should have one attribute, privileges,
# that stores a list of strings as described in Exercise 9-7.
# Move the show_privileges() method to this class.
# Make a Privileges instance as an attribute in the Admin class.
# Create a new instance of Admin and use your method to show its privileges.

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

class Priviledges():
    def __init__(self, priviledges):
        '''Initialize priviledge attribute.'''
        self.priviledges = priviledges
        priviledges = ['can add post', 'can delete posts', 'can ban user', 'can change settings']

    def show_priviledges(self):
        number = 0
        print(f'The user has the following priviledges:')
        for item in self.priviledges:
            number += 1
            print(f'{number}. {item}.')        

class Admin(User):
    def __init__(self, age, first_name, last_name, middle_name='', hometown=''):
        super().__init__(age, first_name, last_name, middle_name, hometown)
        self.priviledges = Priviledges(self)
    

user_1 = Admin(22, 'justice', 'kamwanja', hometown='eldoret')
user_1.priviledges.show_priviledges()