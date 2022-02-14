with open('1A.txt') as F:
    f = F.readlines()
    f.pop(0)
    nums = list(map(lambda s: list(map(int, s.split(' '))), f))

    sumFin = 0
    minDiff = 100000000

    for i in nums:
        x, y = i
        sumFin += max(i)

        currentDiff = abs(x - y)
        if currentDiff != 0 and currentDiff % 10 != 0:
            minDiff = min(currentDiff, minDiff)

    if sumFin % 10 == 0:
        sumFin = sumFin - minDiff
    print(sumFin)
    print(sumFin % 10)

# Ответ: 115997 133967939 (там ошибка в ответах)
