# Write a function called make_shirt() that accepts a size and the
# text of a message that should be printed on the shirt.
# The function should print a sentence summarizing the size of the shirt and the message printed on it.
# Call the function once using positional arguments to make a shirt.
# Call the function a second time using keyword arguments.

def make_shirt(shirt_size, shirt_text):
    print(f"\nThe shirt's size is {shirt_size}. \nThe message '{shirt_text}' will be printed on it. \n")
    
make_shirt(14, 'hello')

make_shirt(shirt_text = 'Happy Holidays!!', shirt_size = 20)