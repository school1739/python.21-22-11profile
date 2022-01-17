# https://inf-ege.sdamgia.ru/problem?id=38602
with open(r'6.txt') as F:
    s = F.read()
    c = 1
    mx = 0

    for i in range(len(s) - 1):
        if s[i] != 'P' or s[i + 1] != 'P':
            c += 1
        else:
            mx = max(mx, c)
            c = 1

    print(mx)
