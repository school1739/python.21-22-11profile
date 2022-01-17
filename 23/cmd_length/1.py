# https://inf-ege.sdamgia.ru/problem?id=3301
paths = []


def f(x, y):
    if x > y:
        return 0
    if x == y:
        return 1
    p = f(x + 2, y) + f(x * 3, y)
    paths.append(p)
    return p


print(f(2))
