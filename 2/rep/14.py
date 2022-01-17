print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not(((z <= y) == (w <= x)) or (x and z)):
                    print(x, y, z, w)
# xwzy
