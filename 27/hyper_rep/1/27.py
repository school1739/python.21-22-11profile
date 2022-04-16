s = 0
remainders = [0] + [None] * 50
lens = [0] + [None] * 50
results = []
with open('27B.txt') as F:
    for i in range(1, int(F.readline())):
        x = int(F.readline())
        s += x
        if remainders[s % 51] != None:
            # Если просят минимальную длинну - храни отрицательное. Если наибольшую - храни положительную
            results.append([s - remainders[s % 51], -1 * (i - lens[s % 51])])
        else:
            remainders[s % 51] = s
            lens[s % 51] = i

print(max(results))
