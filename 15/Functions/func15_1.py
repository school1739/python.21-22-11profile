# coding=UTF8

# ¬ДЕЛ(x, А) → (ДЕЛ(x, 6) → ¬ДЕЛ(x, 4))
# A - max
# https://inf-ege.sdamgia.ru/problem?id=8106
# Ответ: 12

def d(x, a):
    return x % a == 0


# A = 1

# while True:
#     for x in range(1, 1001):
#         if not ((not d(x, A)) <= (d(x, 6) <= (not d(x, 4)))):
#             break
#     else:
#         print(A)
#     A += 1

for A in range(1000, 1, -1):
    for x in range(1, 1001):
        if not ((not d(x, A)) <= (d(x, 6) <= (not d(x, 4)))):
            break
    else:
        print(A)
        break
