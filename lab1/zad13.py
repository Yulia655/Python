def extra_enumerate(arr):
    for i in range(len(arr)):
        elem = arr[i]
        cum = 0
        for j in range(i + 1):
            cum += arr[j]

        frac = cum / sum(arr)
        yield i, elem, cum, frac


x = [1, 3, 4, 2]
for i, elem, cum, frac in extra_enumerate(x):
    print(elem, cum, frac)

#Complete
