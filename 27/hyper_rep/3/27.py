curEvenLen = 0
s = 0
results = []
remainders = [0] + [None] * 16
sums = [0] + [None] * 16
with open('27B.txt') as F:
    for i in range(int(F.readline())):
        x = int(F.readline())
        if x % 2 == 0:
            curEvenLen += 1
        s += x

        # Если ещё не найдено такой подпоследовательности,
        # чья длинна была бы кратна 17, то запишем её.
        if remainders[curEvenLen % 17] == None:
            remainders[curEvenLen % 17] = curEvenLen
            sums[curEvenLen % 17] = s

        # Если такая подпоследовательность найдена, отсекаем
        # от нее столько элементов, сколько нужно, чтобы кол-во
        # чётных элементов стало кратно 17 и cчитаем ее сумму
        else:
            results.append([curEvenLen - remainders[curEvenLen %
                           17], s - sums[curEvenLen % 17]])
print(max(results))

# Ответ: 68377 69972065
