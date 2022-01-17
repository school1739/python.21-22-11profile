from itertools import *
c = 0
for i in product('AEY', repeat=5):
    c += 1
    if c == 60:
        print("".join(i))
# AYAEY
