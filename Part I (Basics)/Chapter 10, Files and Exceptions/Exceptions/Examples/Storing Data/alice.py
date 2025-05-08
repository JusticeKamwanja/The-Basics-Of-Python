filename = 'alice.txt'
try:
    with open(filename) as f_obj:
        contents = f_obj.read()

except FileNotFoundError:
    msg = f'{filename} does not exist.'
    print(msg)

else:
    # Count the number of words in the file.
    words = contents.split()
    word_count = len(words)
    print(words)

    print(f'\nThe file {filename} contains the following {word_count} words: \n')

    number = 0
for word in words:
    number += 1
    while True:
        if word[-1] == '.':
            word = word[:-1]
        else:
            break
    
    print(f'{number}. {word}')