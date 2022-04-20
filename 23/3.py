# https://inf-ege.sdamgia.ru/problem?id=3660
from functools import lru_cache

nums = set()


@lru_cache(None)
def f(x, y):
    if y > 30 or x < 0:
        return 0
    if y == 30:
        nums.add(x)
    return f(x + 5, y + 1) + f(x - 3, y + 1)


f(4, 0)
print(len(nums))
