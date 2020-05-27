def process_adress(adress):
	if adress.startswith('www') and not adress.endswith('.com'):
		return 'http://' + adress + '.com'
	elif adress.startswith('www'):
		return 'http://' + adress
	else: return adress


adresses = [
    'www.vk.com',
    'spases.ru',
    'facebook.com',
    'www.yandex.ru'
]

adresses = [process_adress(adress) for adress in adresses]
print(adresses)

#Complete
