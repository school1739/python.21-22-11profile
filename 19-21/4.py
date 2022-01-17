# https://inf-ege.sdamgia.ru/problem?id=27747

from functools import lru_cache


def moves(h1, h2):
    return (h1 + 1, h2), (h1 * 4, h2), (h1, h2 + 1), (h1, h2 * 4)


@lru_cache(None)
def f(h1, h2):
    def next(*cond):
        return [f(*m) in cond for m in moves(h1, h2)]

    if h1 + h2 >= 82:
        return 'W'
    if any(next('W')):
        return 'P1'
    if any(next('P1')):
        return 'V1'
    if any(next('V1')):
        return 'P2'
    if all(next('P1', 'P2')):
        return 'V2'


print([i for i in range(1, 78) if f(4, i) == 'V1'])
print([i for i in range(1, 78) if f(4, i) == 'P2'])
print([i for i in range(1, 78) if f(4, i) == 'V2'])
