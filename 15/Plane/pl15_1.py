# coding=UTF8

# (x + 2y < A) ∨ (y > x) ∨ (x > 20)
# A - min
# https://inf-ege.sdamgia.ru/problem?id=23916
# Ответ: 61

A = 1

while True:
    for x in range(0, 1000):
        for y in range(0, 1000):
            if not ((x + 2 * y < A) or (y > x) or (x > 20)):
                break
        else:
            continue
        break
    else:
        print(A)

    A += 1
