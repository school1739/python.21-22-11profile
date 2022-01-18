# https://inf-ege.sdamgia.ru/problem?id=36879
f = list(filter(lambda l: l.count('G') < 25, open('5.txt').readlines()))
maxdists = []
for s in f:
    m = {}
    for i in range(len(s)):
        if s.count(s[i]) < 2:
            continue
        else:
            positions = []
            for j in range(len(s)):
                if s[j] == s[i]:
                    positions.append(j)

            m.update({s[i]: max(positions) - min(positions)})
    maxdists.append(max(m.values()))
print(max(maxdists))
