print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if (w <= x) and ((y and z) == (x or y)):
                    print(x, y, z, w)
# yxzw
