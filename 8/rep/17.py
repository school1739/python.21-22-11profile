from itertools import *
c = 0
for i in permutations('ABCDEFG', 5):
    for j in range(len(i) - 1):
        if i[j] in 'BCDFG' and i[j + 1] in 'BCDFG':
            break
    else:
        c += 1
print(c)
# 120
