sum_final = 0
min_diff = 10000000000
with open('3B.txt') as F:
    f = F.readlines()
    f.pop(0)

    for i in f:
        a, b = map(int, i.split(' '))
        diff = abs(a - b)
        if diff % 16 != 0:
            min_diff = min(min_diff, diff)
        sum_final += max(a, b)

if sum_final % 16 != 12:
    print(sum_final)
else:
    print(sum_final - min_diff)

# print(sum_final)
# print(sum_final % 16)

# Ответ: 64390 6664683
