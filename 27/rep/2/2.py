with open('2B.txt') as F:
    f = F.readlines()
    f.pop(0)
    nums = list(map(lambda s: list(map(int, s.split(' '))), f))

    sumFin = 0
    minDiff = 1000000000
    for i in nums:
        x, y = i
        sumFin += min(i)

        currentDiff = abs(x - y)
        if currentDiff != 0 and currentDiff % 100 != 0:
            minDiff = min(currentDiff, minDiff)

    if sumFin % 100 == 0:
        sumFin += minDiff

    print(sumFin)
    print(sumFin % 100)

# Ответ: 34601 3318701
