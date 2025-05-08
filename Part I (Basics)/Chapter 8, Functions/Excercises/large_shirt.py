# Modify the make_shirt() function so that shirts are large
# by default with a message that reads I love Python.
# Make a large shirt and a medium shirt with the default message,
# and a shirt of any size with a different message.

def make_shirt(shirt_text = 'Python', shirt_size = 'Large'):
    print(f"\nThe shirt's size is {shirt_size}. \nThe message '{shirt_text}' will be printed on it. \n")

make_shirt()
make_shirt(shirt_size = 'medium')

make_shirt(shirt_size = 'small', shirt_text = 'Woah')