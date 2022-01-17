with open(r'3.txt') as F:
    mx = 0
    c = 0
    s = F.read()

    for i in range(len(s)):
        if s[i] not in "BC":
            c += 1
        else:
            mx = max(mx, c)
            c = 1

    print(mx)
# Ответ: 26
