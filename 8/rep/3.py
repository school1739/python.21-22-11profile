from itertools import *
c = 0
for i in product('DLORW', repeat=5):
    c += 1
    if "".join(i)[0] == 'W':
        print(c)
        break
# 2501
