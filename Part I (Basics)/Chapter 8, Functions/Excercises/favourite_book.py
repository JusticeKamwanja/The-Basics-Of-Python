# Write a function called favorite_book() that accepts one parameter, title.
# The function should print a message, such as 'One of my favorite books is Alice in Wonderland'.
# Call the function, making sure to include a book title as an argument in the function call.

def favourite_book(title):
    print(f'{title.title()} is one of my favourite books.')


print('Do you know which book I like?')
favourite_book('Alice in Wonderland')