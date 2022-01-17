with open(r'3.txt') as F:
    f = F.readlines()
    n, k, m = map(int, f.pop(0).split(' '))
    f = list(map(int, f))
    f.sort(reverse=True)
    winners = f[:k]
    prizer = f[k:k+m]

    print(int(sum(prizer) / len(prizer)), min(winners))

# Ответ: 722 909

# Другое решение:
# with open("3.txt") as F:
#     n, k, m = map(int, F.readline().split())
#     a = []
#     for i in range(n):
#         a.append(int(F.readline()))
#         a.sort(reverse=True)
#     z = a[k:k+m]
#     sr = int(sum(z)/m)
#     print(sr, a[k-1])
