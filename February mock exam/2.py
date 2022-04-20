print('z y x w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not ((w == z) or (x and (not z)) or w):
                    print(z, y, x, w)
# 1 1 1 0
# 1 0 1 0
# 1 1 0 0
# Ответ: zyxw
