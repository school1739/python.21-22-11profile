for i in range(1000):
    s = i
    n = 1
    while s <= 70:
        s += 9
        n *= 7
    if n == 343:
        print(i)
        break
