summ_final = 0
min_diff = 100000
with open('2B.txt') as F:
    f = F.readlines()
    f.pop(0)
    for i in f:
        a, b = map(int, i.split(' '))
        diff = abs(a-b)
        if diff % 100 != 0:
            min_diff = min(diff, min_diff)
        summ_final += min(a, b)

if summ_final % 100 == 0:
    print(summ_final + min_diff)
else:
    print(summ_final)

# Ответ: 34601 3318701
