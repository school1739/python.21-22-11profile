from itertools import *
c = 0
for i in product('ABCDEFGHIJ', repeat=3):
    c += 1
    if "".join(i) == 'GIA':
        print(c)
# 681
