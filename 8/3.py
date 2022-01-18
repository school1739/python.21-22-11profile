from itertools import *

c = 0
for i in product('КУРИЦА', repeat=5):
    if i.count('У') >= 2:
        c += 1

print(c)
