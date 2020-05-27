password = input('Password: ')
contains_uppercase_sym = False
contains_lowercase_sym = False
contains_figures = False
reliability_points = 0

if len(password) < 8:
    reliability_points += 1
elif len(password) < 14:
    reliability_points += 2
else:
    reliability_points += 4

for sym in password:
    if contains_uppercase_sym and contains_lowercase_sym and contains_figures:
        reliability_points += 6
        break

    if sym.isupper():
        contains_uppercase_sym = True
    elif sym.islower():
        contains_lowercase_sym = True
    elif sym.isdigit():
        contains_figures = True
else:
    if contains_uppercase_sym:
        reliability_points += 2
    if contains_lowercase_sym:
        reliability_points += 2
    if contains_figures:
        reliability_points += 2

if reliability_points < 5:
    print('Weak')
elif reliability_points <= 8:
    print('Normal')
else:
    print('Strong')

#Complete
