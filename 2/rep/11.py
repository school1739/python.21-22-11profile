print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not ((((not y) == x) <= (y and z)) or ((not z) and w)):
                    print(x, y, z, w)
# yxzw
