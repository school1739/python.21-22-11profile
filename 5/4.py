#https://inf-ege.sdamgia.ru/problem?id=18554

for i in range(1000000):
    n = i
    n = bin(n)[2:]
    if n.count('1') > n.count('0'):
        n = str(n) + '1'
        n = int(n, base=2)
    else:
        n = str(n) + '0'
        n = int(n, base=2)
        if n > 80:
            print(n)
            break

#Ответ: 82
