# https://inf-ege.sdamgia.ru/problem?id=27882

f = sorted([int(i) for i in open('26.txt').readlines()])
f.pop(0)
fSet = set(f)
evenNumbers = list(filter(lambda n: n % 2 == 0, f))

c = 0
mx = 0

for i in range(len(evenNumbers) - 1):
    for j in range(i + 1, len(evenNumbers)):
        average = (evenNumbers[i] + evenNumbers[j]) / 2
        if average in fSet:
            c += 1
            mx = max(mx, average)

print(c, mx)
