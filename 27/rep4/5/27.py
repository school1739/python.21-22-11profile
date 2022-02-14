with open('A.txt') as F:
    f = list(map(int, F.readlines()))
    f.pop(0)

    wait = f[:6]
    odd, even, pairs = 0, 0, 0

    for i in range(6, len(f)):
        if wait[0] % 2 == 0:
            even += 1
        else:
            odd += 1

        x = f[i]
        if x % 2 == 0:
            pairs += odd
        else:
            pairs += even

        del wait[0]
        wait.append(x)

    print(pairs)
