print('x y z F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            if not ((x or (not(y))) <= (y == z)):
                print(x, y, z, 0)
