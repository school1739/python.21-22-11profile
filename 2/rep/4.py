print('x y z w')

for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not (w or ((not x) or (not z)) and ((not x) or y or z)):
                    print(x, y, z, w)
