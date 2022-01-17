from itertools import *
c = 0
for i in product("EILMS", repeat=5):
    c += 1
    if "".join(i) == "SMILE":
        print(c)
# 2911
