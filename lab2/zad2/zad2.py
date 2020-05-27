import os
import hashlib

path = os.getcwd()  #input()
sum_dict = {}
for root, dirs, files in os.walk(path):
    for file in files:
        path = os.path.join(root, file)
        with open(path, 'r') as f:
            content = f.read().encode('utf-8')

        checksum = hashlib.md5(content).hexdigest()
        if checksum in sum_dict:
            sum_dict[checksum] += [path]
        else:
            sum_dict[checksum] = [path]

sum_dict = {sum: group for sum, group in sum_dict.items() if len(group) > 1}
counter = 1
for group in sum_dict.values():
    print('Group {}:'.format(counter))
    for path in group:
        print(path)

    counter += 1
    print()

#Complete
