# https://inf-ege.sdamgia.ru/problem?id=28080

from functools import lru_cache


def moves(rocks):
    return rocks + 1, rocks + 2, rocks * 2


@lru_cache(None)
def f(rocks):
    def next(*cond):
        return [f(m) in cond for m in moves(rocks)]

    if rocks >= 36:
        return 'W'
    if any(next('W')):
        return 'P1'
    if all(next('P1')):
        return 'V1'
    if any(next('V1')):
        return 'P2'
    if all(next('P1', 'P2')):
        return 'V2'


print([i for i in range(1, 35) if f(i) == 'V1'])
print([i for i in range(1, 35) if f(i) == 'P2'])
print([i for i in range(1, 35) if f(i) == 'V2'])
