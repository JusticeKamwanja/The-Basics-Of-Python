# Add an attribute called login_attempts to your User class from Exercise 9-3 (page 166).

from random import choice

class User():
    def __init__(self, age, first_name, last_name, login_attempts):
        
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = login_attempts

    def describe_user(self):
        print(f'\nHere is some information about the user:')
        print(f'The user is called {self.first_name.title()} {str(self.middle_name.title())} {self.last_name.title()}.')
        if self.hometown:
            print(f'{self.first_name.title()} is a {self.age} year old from {self.hometown.title()}. \n')

        else:
            print(f'{self.first_name.title()} is a {self.age} year old. \n')

        print(f'{self.first_name.title()} has attempted to log in {self.login_attempts} times. \n')
        
    def show_login_attempts(self):
        if self.login_attempts <= 0:
            print(choice([
                f'{self.first_name.title()} has not made any login attempt. \n',
                f'{self.first_name.title()} has not made any login attempt whatsoever. \n',
                f'{self.first_name.title()} has made zero login attempts. \n',
                f'{self.first_name.title()} has made {self.login_attempts} login attempts. \n',
                f'{self.first_name.title()} has not made a single login attempt. \n',
                f'{self.first_name.title()} has not logged in. \n',
                f'{self.first_name.title()} has not logged in at all. \n',
                ]))

        elif self.login_attempts == 1:
            print(choice([
                f'{self.first_name.title()} has made a single login attempt. \n'
                f'{self.first_name.title()} has made {self.login_attempts} login attempt. \n'
                f'{self.first_name.title()} has made just {self.login_attempts} login attempt. \n'
                f'{self.first_name.title()} has made only {self.login_attempts} login attempt. \n'

                ]))

        else:
            print(f'{self.first_name.title()} has made {self.login_attempts} login attempts. \n')

    # A method that increments the value of login_attempts by 1.
    def increment_login_attempts(self):
        self.login_attempts += 1

    # A method that resets the value of login_attempts to 0.
    def reset_login_attempts(self):
        self.login_attempts = 0

# Make an instance of the User class and call increment_login_attempts() several times.
justice = User(22, 'justice', 'kamwanja', 5)

justice.increment_login_attempts()
justice.increment_login_attempts()
justice.increment_login_attempts()
justice.increment_login_attempts()

# Print the value of login_attempts to make sure it was incremented properly, 
justice.show_login_attempts()

# and then call reset_login_attempts().
justice.reset_login_attempts()

# Print login_attempts again to make sure it was reset to 0.
justice.show_login_attempts()
justice.show_login_attempts()
justice.show_login_attempts()
justice.show_login_attempts()
justice.show_login_attempts()