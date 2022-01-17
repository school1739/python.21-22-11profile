from itertools import *
c = 0
for i in product('1234567890', repeat=4):
    pairs = 0
    for j in range(len(i) - 1):
        if i[j] == i[j + 1] and i.count(i[j]) == 2:
            pairs += 1
    if pairs == 1:
        c += 1
print(c)
# 2250
