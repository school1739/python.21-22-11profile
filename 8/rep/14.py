# Вариант 1
# from itertools import *
# c = 0
# for i in product('123456789', repeat=3):
#     if len(set(i)) == 3:
#         c += 1
# print(c)
# Вариант 2
from itertools import *
c = 0
for i in permutations('123456789', 3):
    c += 1
print(c)
# 504
