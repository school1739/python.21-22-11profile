# https://inf-ege.sdamgia.ru/problem?id=39763
with open("17.txt") as f:
    num = [int(l) for l in f]
    c = 0
    s = -1
    for i in range(2, len(num)):
        if num[i]**2 < num[i-1]**2+num[i-2]**2 and \
                num[i-1]**2 < num[i]**2+num[i-2]**2 and \
                num[i-2]**2 < num[i-1]**2+num[i]**2:
            c += 1
            s = max(s, num[i] + num[i-1] + num[i-2])
    print(c, s)

# Ответ: 1175 29451
