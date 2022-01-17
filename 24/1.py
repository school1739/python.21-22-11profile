# https://inf-ege.sdamgia.ru/problem?id=27421
with open(r'1.txt') as F:
    s = F.read()
    c = 1
    mx = -1
    for i in range(len(s) - 1):
        if s[i] != s[i + 1]:
            c += 1
        else:
            mx = max(mx, c)
            c = 1
    print(mx)
    
# Ответ: 35
