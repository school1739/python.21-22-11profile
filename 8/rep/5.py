from itertools import *
c = 0
for i in product('ABCDEFGH', repeat=3):
    c += 1
    if c == 480:
        print("".join(i))
        break
# HDH
