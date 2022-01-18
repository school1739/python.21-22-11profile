# https://inf-ege.sdamgia.ru/problem?id=37337
# Задание предложил Антон

with open("17 (1).txt") as s:
    numbers = [int(x) for x in s]
    f = []
    for i in range(0,len(numbers)):
        for j in range(i+1, len(numbers)):
            if  (numbers[i]%160 != numbers[j]%160) and (numbers[i]%7==0 or numbers[j]%7==0):
                f.append(numbers[i]+numbers[j])
    print(len(f), max(f))
# Ответ: 12749665 19989