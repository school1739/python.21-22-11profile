from itertools import *

c = 0
for i in set(permutations('ЛАГЕРЬ')):
    if i[0] != 'Ь' and ('ЕА' not in "".join(i)):
        c += 1

print(c)
# Ответ: 504
