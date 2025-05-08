def greet_user(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        message = "Hello " + name.title() + '. How are you doing? \n'
        print(message)

usernames = ['Michael', 'Daisy', 'Brian', 'Polly']

greet_user(usernames)