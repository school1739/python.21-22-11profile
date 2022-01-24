sum_final = 0
min_diff = 100000000

with open('4A.txt') as F:
    f = F.readlines()
    f.pop(0)

    for i in f:
        cord = sorted(map(int, i.split(' ')))

        diff = abs(cord[2] - cord[0])
        if diff % 18 != 0:
            min_diff = min(diff, min_diff)

        diff = abs(cord[2] - cord[1])
        if diff % 18 != 0:
            min_diff = min(diff, min_diff)

        sum_final += cord[0] + cord[1]

if sum_final % 18 == 0:
    print(sum_final + min_diff)
else:
    print(sum_final)

# Ответ: 35645 3722077
