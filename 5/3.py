#https://inf.reshuege.ru/problem?id=13482

for i in range(1, 10000, 1):
    x = i
    if x % 2 == 1:
        a = str(x % 4)
        b = str(x % 3)
        c = str(x % 2)
        y = a + b + c
        if int(y) == 301:
            print(x)

#Ответ: 15
