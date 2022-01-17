print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not ((not y) or x or (z and (not w))):
                    print(x, y, z, w, 0)
