from itertools import *
c = 0
for i in product('MIND', repeat=6):
    if "".join(i).count('N') <= 1:
        c += 1

print(c)
