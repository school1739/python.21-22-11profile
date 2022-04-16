s = 0
results = []
remainders = [0] + [None] * 120
lens = [0] + [None] * 120

with open('27B.txt') as F:
    for i in range(1, int(F.readline())):
        x = int(F.readline())
        s += x

        # Еще остаток записан, то сохраняем подпоследовательность за вычетом наименьшей суммы, которая
        # нужна, чтобы сумма стала кратна 121
        if remainders[s % 121] != None:
            results.append([s - remainders[s % 121], i - lens[s % 121]])
        # Еще не записан остаток, то пишем наименьший (сумма тогда наибольшая)
        # Длинну сохраняем как i
        else:
            remainders[s % 121] = s
            lens[s % 121] = i

print(max(results))

# Ответ: 88 99985
