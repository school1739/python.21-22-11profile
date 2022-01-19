# https://inf-ege.sdamgia.ru/problem?id=18785

for i in range(1, 10000):
    n = i
    r = bin(n)[2:]
    if n % 2 == 0:
        r = '1' + r + '0'
    else:
        r = '11' + r + '11'

    if (int(r, 2) > 52):
        print(n)
        break

# Ответ: 3
