with open('B.txt') as F:
    f = list(map(int, F.readlines()))
    f.pop(0)

    wait = f[:7]
    div14, div7, div2, none, pairs = 0, 0, 0, 0, 0

    for i in range(7, len(f)):
        if wait[0] % 14 == 0:
            div14 += 1
        elif wait[0] % 7 == 0:
            div7 += 1
        elif wait[0] % 2 == 0:
            div2 += 1
        else:
            none += 1

        x = f[i]
        if x % 14 == 0:
            pairs += div14 + div7 + div2 + none
        elif x % 7 == 0:
            pairs += div14 + div2
        elif x % 2 == 0:
            pairs += div14 + div7
        else:
            pairs += div14

        del wait[0]
        wait.append(x)

    print(pairs)
