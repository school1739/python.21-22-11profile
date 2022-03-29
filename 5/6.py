#https://inf-ege.sdamgia.ru/problem?id=16435

for i in range(2, 10000):
    n = i
    n = bin(n)[2:]
    r = len(n) - 1
    n = n[0:r]
    if i % 2 != 0:
        n = str(n) + '10'
    else:
        n = str(n) + '01'
    if int(n, base=2) == 2017:
        print(i)

#Ответ: 1008