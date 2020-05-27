import re
#import string

class StringFormatter(object):
    separators = [' ']

    @staticmethod
    def _get_words(line):
        return re.split('|'.join(StringFormatter.separators), line)

    @staticmethod
    def clean(line, n):
        words = StringFormatter._get_words(line)
        new_string_parts = [word for word in words if len(word) > n]
        return ' '.join(new_string_parts)

    @staticmethod
    def hide_figures(line):
        #return line.translate(string.maketrans('0123456789', '**********'))
        for num in '0123456789':
            line = line.replace(num, '*')

        return line

    @staticmethod
    def add_spases(line):
        return line.replace('', ' ')

    @staticmethod
    def sort_by_size(line):
        words = StringFormatter._get_words(line)
        return ' '.join(sorted(words, key=lambda word: len(word)))

    @staticmethod
    def sort_by_lec(line):
        words = StringFormatter._get_words(line)
        return ' '.join(sorted(words))


if __name__ == '__main__':
    s = 'hfdkfh jhgjf ghjf 345h djhf lknhj 7854 fhui9 ghjf j'
    print(StringFormatter.clean(s, 4))
    print(StringFormatter.hide_figures(s))
    print(StringFormatter.add_spases(s))
    print(StringFormatter.sort_by_size(s))
    print(StringFormatter.sort_by_lec(s))

#Complete
