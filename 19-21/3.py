# https://inf-ege.sdamgia.ru/problem?id=27416

from functools import lru_cache


def moves(h1, h2):
    return (h1 + 1, h2), (h1, h2 + 1), (h1 * 2, h2), (h1, h2 * 2)


@lru_cache(None)
def f(h1, h2):
    def next(*cord):
        return [f(*m) in cord for m in moves(h1, h2)]

    if h1 + h2 >= 77:
        return 'W'
    if any(next('W')):
        return 'P1'
    if any(next('P1')):
        return 'V1'
    if any(next('V1')):
        return 'P2'
    if all(next('P1', 'P2')):
        return 'V2'


print([i for i in range(1, 70) if f(7, i) == 'V1'])
print([i for i in range(1, 70) if f(7, i) == 'P2'])
print([i for i in range(1, 70) if f(7, i) == 'V2'])
