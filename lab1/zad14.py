def non_empty(func):
    def dec():
        return list(filter(lambda el: el != '' and el is not None, func()))
    return dec


@non_empty
def get_pages():
    return ['chapter1', '', 'contents', '', 'line1', None]


print(get_pages())

#Complete
