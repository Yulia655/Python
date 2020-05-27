with open('sample1.txt', 'rt') as f:
    inner_text = f.read()

text_without_puncmarks = [ch.lower() for ch in inner_text if ch.isalpha()]
text_letters = list(set(text_without_puncmarks))
sort_key = lambda ch: text_without_puncmarks.count(ch)
text_letters.sort(key=sort_key, reverse=True)
for letter in text_letters:
    print(letter, text_without_puncmarks.count(letter))

#Complete
