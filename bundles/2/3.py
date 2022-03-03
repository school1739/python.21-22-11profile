for i in range(105000, 135200 + 1):
    nums = set()
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            n = 2
            while j**n < i:
                n += 1
            if j ** n == i and n >= 3:
                print(i, j, n)
