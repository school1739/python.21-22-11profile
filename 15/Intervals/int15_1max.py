# coding=UTF8

# P = [2, 10] и Q = [6, 14]
# ((x ∈ А) → (x ∈ P)) ∨ (x ∈ Q)
# len(A) - max
# https://inf-ege.sdamgia.ru/problem?id=34534

def f(x, A):
    return ((x in A) <= (x in P)) or (x in Q)


p1, p2, q1, q2 = 2, 10, 6, 14
P = [i / 10 for i in range(p1 * 10, p2 * 10 + 1)]
Q = [i / 10 for i in range(q1 * 10, q2 * 10 + 1)]

A = set([i / 10 for i in range(10, 150 + 1)])

for x in [i / 10 for i in range(10, 150 + 1)]:
    if not f(x, A):
        A.remove(x)

print(sorted(A))

# Ответ: 12
