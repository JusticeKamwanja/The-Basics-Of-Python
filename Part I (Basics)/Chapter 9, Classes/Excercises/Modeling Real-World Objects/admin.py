# An administrator is a special kind of user.
# Write a class called Admin that inherits from the User class you wrote in Exercise 9-3 (page 166) or Exercise 9-5 (page 171).
# Add an attribute, privileges, that stores a list of strings like 
# "can add post", "can delete post", "can ban user", and so on.
# Write a method called show_privileges() that lists the administrator’s set of privileges.
# Create an instance of Admin, and call your method.

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

class Admin(User):
    def __init__(self, age, first_name, last_name, middle_name='', hometown=''):
        super().__init__(age, first_name, last_name, middle_name, hometown)

        self.priviledges = ['can add post', 'can delete posts', 'can ban user', 'can change settings']

    def show_priviledges(self):
        number = 0
        print(f'Admin {self.first_name.title()} has the following priviledges:')
        for item in self.priviledges:
            number += 1
            print(f'{number}. {item}.')
    

user_1 = Admin(22, 'justice', 'kamwanja', hometown='eldoret')
user_1.show_priviledges()