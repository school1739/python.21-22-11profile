# https://inf-ege.sdamgia.ru/problem?id=18558
from itertools import *
c = 0
for i in product('ИВАН', repeat=5):
    if i.count('И') >= 1:
        c += 1

print(c)
# Ответ: 781
