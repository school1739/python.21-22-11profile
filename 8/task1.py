from itertools import *

c = 0
for i in product('СУМКА', repeat=4):
    if i.count('У') >= 1:
        c += 1
print(c)
# Ответ: 369
