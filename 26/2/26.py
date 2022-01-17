# https://inf-ege.sdamgia.ru/problem?id=27882

f = open('26.txt').readlines()

s = int(f[0].strip().split(' ')[0])
n = int(f[0].strip().split(' ')[1])

f.pop(0)

f = [int(i) for i in f]

f.sort()

t = 0
c = 0
for i in f:
    t += i
    if t >= s:
        break
    else:
        c += 1

print(c, end=' ')

mxel = f[0]
for i in range(len(f)):
    strip = f[0:i]
    if sum(strip) < s:
        mxel = f[i]
    else:
        break
print(mxel)
