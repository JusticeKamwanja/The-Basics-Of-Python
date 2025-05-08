filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming, it's just interesting.")
    file_object.write('\nI love creating new games.')

with open(filename, 'a') as file_object:
    file_object.write("\nI also love finding meaning in large datasets.")
    file_object.write("\nI love creating apps that can run in a browser.")