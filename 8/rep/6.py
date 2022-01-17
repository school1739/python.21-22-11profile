from itertools import *
c = 0
for i in product('AINRT', repeat=5):
    c += 1
    if c == 710:
        print("".join(i))
        break
# IARIT
