for a in range(1, 1000):
    fl = True
    for x in range(1, 1000):
        for y in range(1, 1000):
            if ((2 * y + 3 * x != 135) or (y > a) or (x > a)) == False:
                fl = False
                break
        if fl == False:
            break
    if fl == True:
        print(a)
