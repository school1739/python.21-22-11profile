with open(r'2.txt') as F:
    f = F.readlines()
    n, k = map(int, f.pop(0).split(' '))
    f = list(map(int, f))
    f.sort(reverse=True)
    excel = f[:k]
    good = f[k:k*2]
    eAvrg = int(sum(excel) / len(excel))
    gAvrg = int(sum(good) / len(good))

    print(gAvrg, eAvrg)

# Ответ: 856 953

# Другое решение:
# with open("2.txt") as F:
#     n, k = map(int, F.readline().split())
#     a = []
#     for i in range(n):
#         a.append(int(F.readline()))
#         a.sort(reverse=True)
#     b = a[:k]
#     c = a[k:2 * k]
#     s5 = int(sum(b) / len(b))
#     s4 = int(sum(c) / len(c))
#     print(s4, s5)
