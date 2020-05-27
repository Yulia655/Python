STRING = '''Пророк брошура крекер крен
рефрактор руль квартира рисора трувер
версус прораб ресурс придира kek'''

words = STRING.split()
short = list(filter(lambda x: len(x) < 4, words))
medium = list(filter(lambda x: 4 <= len(x) < 7, words))
long = list(filter(lambda x: len(x) >= 7, words))

print(short)
print(medium)
print(long)

#Complete
