f = open('27B.txt')
n = int(f.readline())
s = 0
res = []
remainders = [0] + [None]*54
remaindersLen = [0] + [None]*54

for i in range(n):
    s += int(f.readline())
    if s % 55 == 0:
        res.append([s, i + 1])
        continue
    if remainders[s % 55] != None:
        res.append([s - remainders[s % 55], i - remaindersLen[s % 55]])
    else:
        remainders[s % 55] = s
        remaindersLen[s % 55] = i

print(max(res)[1])
