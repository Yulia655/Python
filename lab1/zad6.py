ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
text = input('Enter a line: ')
letters = list(filter(lambda l: text.count(l) == 1, ALPHABET))
print(letters)

#Complete
