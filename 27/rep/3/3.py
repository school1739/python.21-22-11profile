def analyzer(path):
    with open(path) as F:
        f = F.readlines()
        f.pop(0)
        nums = list(map(lambda s: list(map(int, s.split(' '))), f))

        sumFin = 0
        minDiff = 1000000000
        for i in nums:
            x, y = i
            sumFin += max(i)
            currentDiff = abs(x - y)
            if currentDiff != 0 and currentDiff % 16 != 12:
                minDiff = min(currentDiff, minDiff)

        if sumFin % 16 == 12:
            sumFin -= minDiff

        return sumFin


print(analyzer('3A.txt'), analyzer('3B.txt'))
# Ответ: 64390 6664683
