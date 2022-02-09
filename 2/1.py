print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                print(x, y, '-', w, int(((w <= (not(x))) == (z <= y)) and (y or w)))
