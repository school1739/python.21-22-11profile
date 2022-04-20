from itertools import product


c = 0
for i in product('0123456', repeat=7):
    if i[0] != '0' and i[0] != '3' and i[0] != '5' \
            and ('22' not in "".join(i) or '44' not in "".join(i)):
        c += 1

print(c)
