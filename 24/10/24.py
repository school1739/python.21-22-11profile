# https://inf-ege.sdamgia.ru/problem?id=40999

with open('24.txt') as F:
    maxLen = 0
    f = F.readline()

    for i in f.split('E'):
        if i.count('A') >= 3:
            maxLen = max(maxLen, len(i))

    print(maxLen)
