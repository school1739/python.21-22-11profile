with open(r'test.txt') as F:
    f = F.readlines()
    d, n = map(int, f.pop(0).split(' '))
    f = list(map(int, f))
    f.sort()
    c = 0
    m = d
    for i in range(len(f)):
        if m >= 0:
            m -= f[i]
            c += 1
        else:
            break
    print(c)
