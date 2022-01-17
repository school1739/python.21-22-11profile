from itertools import *
c = 0
for i in product('HALO', repeat=7):
    if 'A' in "".join(i):
        c += 1

print(c)
# 14197
