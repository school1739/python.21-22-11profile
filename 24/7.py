# https://inf-ege.sdamgia.ru/problem?id=27689
f = open('3.txt').read()
f = f.replace('XYZ', 't')
c = 1
mx = 0
for i in range(len(f) - 1):
    if f[i] == 't' and (f[i + 1] == 't' or f[i + 1] == 'tX' or f[i + 1] == 'tXY'):
        c += 1
    else:
        mx = max(mx, c)
        c = 1

print(mx)

# ОТВЕТ НЕВЕРНЫЙ
