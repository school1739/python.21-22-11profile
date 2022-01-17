from itertools import *
c = 0
for i in permutations('1234567890', 5):
    c += 1
print(c)
# 30240
