from itertools import *
c = 0
for i in permutations('TOUGH', 4):
    if "".join(i)[0] != 'U':
        c += 1

print(c)
# 96
