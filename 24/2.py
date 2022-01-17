# https://inf-ege.sdamgia.ru/problem?id=27686
with open(r'2.txt') as F:
    s = F.read()
    c = 1
    mx = -1
    for i in range(len(s) - 1):
        if s[i] == 'X' and s[i+1] == 'X':
            c += 1
        else:
            mx = max(mx, c)
            c = 1
    print(mx)

