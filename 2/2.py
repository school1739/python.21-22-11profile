# https://inf-ege.sdamgia.ru/problem?id=18614

print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                print(x, y, z, w, int(((w <= (not x)) == (z <= y)) and (y or w)))

# x w y z  F
# 0 0 0 0  0
# 0 0 0 1  0
# 0 1 0 1  0
# 0 0 1 0  1
# 0 1 1 0  1
# 0 1 1 1  1
# 1 0 0 0  0
# 1 1 0 0  0
# 1 0 0 1  0
# 1 1 0 1  1
# 1 0 1 0  1
# 1 1 1 0  0 #
# 0 0 1 1  1 #
# 0 1 0 0  1 #
# 1 0 1 1  1
# 1 1 1 1  0
