from itertools import *
c = 0
for i in product('WXYZ', repeat=6):
    if "".join(i).count('Y') == 2:
        c += 1

print(c)
# 1215
