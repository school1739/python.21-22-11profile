sum_final = 0
min_diff = 10000000
with open("1B.txt") as F:
    f = F.readlines()
    f.pop(0)
    for i in f:
        a, b = map(int, i.split(' '))
        diff = abs(a - b)
        if diff % 10 != 0:
            min_diff = min(diff, min_diff)
        sum_final += max(a, b)

if sum_final % 10 != 0:
    print(sum_final)
else:
    print(sum_final - min_diff)

# Ответ: 115997 133967939
