def gen_str(arr):
    for word in arr:
        if word.istitle():
            yield word.upper()
        else:
            yield word


string = 'We wish you a Merry Christmas'
words = string.split()

print(' '.join(list(gen_str(words))))

#Complete
