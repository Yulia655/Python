denominations = {1000: 40, 100: 60, 50: 70, 10: 100}
money = int(input('Money for removal: '))

thousands = int(money / 1000)
hundreds = int((money % 1000) / 100)
half_hundreds = 1 if money % 100 > 50 else 0
dozens = int((money % 100 if half_hundreds is 0 else money % 100 - 50) / 10)

try:
    if denominations[1000] < thousands:
        hundreds += (thousands - denominations[1000]) * 10
        thousands = denominations[1000]
        if denominations[100] < hundreds:
            half_hundreds += (hundreds - denominations[100]) * 2
            hundreds = denominations[100]
            if denominations[50] < half_hundreds:
                dozens += (half_hundreds - denominations[50]) * 5
                half_hundreds = denominations[50]
                if denominations[10] < dozens:
                    raise ValueError

    print('{0}*1000 + {1}*100 + {2}*50 + {3}*10'.format(thousands,
                                                        hundreds,
                                                        half_hundreds,
                                                        dozens))
except ValueError:
    print('Операция не может быть выполнена!')

#Complete
