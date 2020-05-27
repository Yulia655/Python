import datetime
import random
import itertools

teams = ['Real Madrid', 'Barcelona', 'Bayern München', 'Juventus',
         'Chelsea', 'Atlético Madrid', 'Borussia Dortmund',
         'Paris Saint Germain',
         'Tottenham Hotspur', 'SSC Napoli', 'Roma', 'Arsenal',
         'Benfica', 'Shakhtar Donetsk', 'Manchester City',
         'Manchester United'
         ]

random.shuffle(teams)
groups = [teams[0: 4], teams[4: 8], teams[8: 12], teams[12: 16]]

num = 1
for group in groups:
    print('Group {}:'.format(num))
    for team in group:
        print(team)

    print()
    num += 1

term = datetime.timedelta(days=14)
match_time = datetime.datetime(2017, 9, 14, 22, 45, 00)

combs = [list(itertools.combinations(group, 2)) for group in groups]
for i in range(3):
    inv = - i - 1
    date = str(match_time).replace('-', '/')
    for comb in combs:
        print(date, ' VS '.join(comb[i]))
        print(date, ' VS '.join(comb[inv]))

    print()
    match_time += term

#Complete
