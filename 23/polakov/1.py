# https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=4126
from functools import lru_cache


@lru_cache(None)
def f(x, y):
    if x > y:
        return 0
    if x == y:
        return 1
    return f(x + 1, y) + f(x + 2, y)


@lru_cache(None)
def f17Only(x, y):
    if x > y or x == 23:
        return 0
    if x == y:
        return 1
    return f17Only(x + 1, y) + f17Only(x + 2, y)


@lru_cache(None)
def f23Only(x, y):
    if x > y or x == 17:
        return 0
    if x == y:
        return 1
    return f23Only(x + 1, y) + f23Only(x + 2, y)


print(
    f17Only(11, 17) * f17Only(17, 29) +
    f23Only(11, 23) * f23Only(23, 29) +
    f(11, 17) * f(17, 23) * f(23, 29)
)
