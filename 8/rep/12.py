from itertools import *
c = 0
for i in product('ABCD123', repeat=4):
    s = "".join(i)
    if (s.count('1') + s.count('2') + s.count('3')) == 1:
        c += 1
print(c)
# 768
