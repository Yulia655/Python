try:
    figure = float(input('Write the figure: '))
    if figure < 0:
        raise TypeError

    rubles = int(figure)
    kopecks = int((figure - rubles) * 100)
    print(rubles, 'руб.', kopecks, 'коп.')
except TypeError:
    print('Error: the figure is smaller than 0!')
except:
    print('Error when converting to float')

#Complete
