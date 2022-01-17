print('x y z w F')

for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not (((y <= z) or (x and w)) == (w <= z)):
                    print(x, y, z, w, 0)
# zyxw
