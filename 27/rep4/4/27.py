with open('A.txt') as F:
    f = list(map(int, F.readlines()))
    f.pop(0)

    wait = f[:5]
    pairs = 0
    remainders = [0]*14

    for i in range(5, len(f)):

        remainders[wait[0] % 14] += 1

        x = f[i]
        pairs += remainders[(14 - x % 14) % 14]
        del wait[0]
        wait.append(x)

    print(pairs)
