with open(r'5.txt') as F:
    s = F.read()
    c = 0
    for i in range(len(s) - 2):
        if s[i] != s[i + 2] and s[i + 1] in 'BCE' and (s[i + 1] == s[i + 2] and s[i + 2] in 'FCE'):
            c += 1
    print(c)
# Ответ: 4659
