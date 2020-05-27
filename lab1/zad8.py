import random

n = random.randint(1, 10000)
print('n =', n)
figure_list = [random.randint(1, 10000) for _ in range(n)]

num = 2
while num < n:
    num *= 2

figure_list += [0] * (num - n)
print('List length:', len(figure_list))
print(figure_list)

#Complete
