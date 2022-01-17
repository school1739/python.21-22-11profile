from itertools import *
c = 0
for i in product('EHMO', repeat=4):
    c += 1
    if 'E' not in "".join(i):
        print(c)
        break
# 86
