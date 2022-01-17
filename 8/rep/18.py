from itertools import *
c = 0
for i in permutations('ABCDEFG', 4):
    if i[0] != 'G' and ('CD' not in "".join(i)):
        c += 1
print(c)
# 668
