# coding=UTF8

# x&25 ≠ 0 → (x&19 = 0 → x&А ≠ 0)
# A - min
# https://inf-ege.sdamgia.ru/problem?id=34511
# Ответ: 8

A = 1

while True:
    for x in range(1, 1000000):
        if not ((x & 25 != 0) <= ((x & 19 == 0) <= (x & A != 0))):
            break
    else:
        print(A)

    A += 1
