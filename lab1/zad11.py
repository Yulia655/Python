def frange(first, last, step):
    while first < last:
        yield round(first, 1)
        first += step


for x in frange(1, 5, 0.1):
    print(x)

#Complete
