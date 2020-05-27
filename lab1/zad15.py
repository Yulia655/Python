def pre_process(a=0.97):

    def _decorator(func):

        def wrap(*args):
            s = args[0]
            for i in range(1, len(s)):
                s[i] -= a * s[i - 1]

            print('a =', a)
            func(s)


        return wrap

    return _decorator


@pre_process(a=0.93)
def plot_signal(s):
    for sample in s:
        print(sample)


arr = [0, 1, 2, 3, 4, 5]
plot_signal(arr)

#Complete
