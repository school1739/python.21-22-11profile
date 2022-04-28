# coding=UTF8

# ¬ДЕЛ(x, А) → (ДЕЛ(x, 6) → ¬ДЕЛ(x, 4))
# A - max
# https://inf-ege.sdamgia.ru/problem?id=8106
# Ответ: 12

def jopanosoroga(x, a):
    return x % a == 0


A = 1

while True:
    for x in range(1, 1001):
        if not ((not jopanosoroga(x, A)) <= (jopanosoroga(x, 6) <= (not jopanosoroga(x, 4)))):
            break
    else:
        print(A)
    A += 1
