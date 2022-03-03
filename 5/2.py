#https://inf.reshuege.ru/problem?id=33084

for i in range(10000):
    n = i
    r = bin(n)[2:]
    r = r + bin(r.count('1') % 2)[2:]
    r = r + bin(r.count('1') % 2)[2:]
    if int(r, 2) > 154:
        print(n)
        break

#Ответ: 39


