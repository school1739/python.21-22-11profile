with open('17.txt') as F:
    c, maxSum = 0, 0
    f = list(map(int, F.readlines()))
    for i in range(len(f) - 1):
        for j in range(i, len(f)):
            if f[i] % 31 == 0 or f[j] % 31 == 0:
                if (f[i] - f[j]) % 2 == 0:
                    c += 1
                    maxSum = max(maxSum, f[i] + f[j])

    print(c, maxSum)
