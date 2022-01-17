from itertools import *
c = 0
for i in product('WXYZ', repeat=5):
    if 0 < "".join(i).count('X') <= 3:
        c += 1

print(c)
# 765
