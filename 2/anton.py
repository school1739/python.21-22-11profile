def F(x, y, z):
    return (not z) and x or x and y


print('x y z F')
for z in range(2):
    for y in range(2):
        for x in range(2):
            print(x, y, z, F(x, y, z))

# z y x
