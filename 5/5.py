# https://inf-ege.sdamgia.ru/problem?id=28542

for i in range(1000):
    res = ''
    s = i
    while s > 0:
        res = str(s % 3) + res
        s //= 3

    r = res + str(i % 3)
    if len(str(int(r, 3))) == 4:
        print(str(int(r, 3)))
        break
