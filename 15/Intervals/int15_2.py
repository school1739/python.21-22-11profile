# Р = [30, 45] и Q = [40, 55]
# len(A) - min

# (¬(x ∈ A) → (¬(x ∈ P)))
# ((x ∈ Q)→ (x ∈ A))

# https://inf-ege.sdamgia.ru/problem?id=34538


def f(x, A):
    return (x not in A) <= (x not in P)


def g(x, A):
    return (x in Q) <= (x in A)


p1, p2, q1, q2 = 30, 45, 40, 55
P = [i / 10 for i in range(p1 * 10, p2 * 10 + 1)]
Q = [i / 10 for i in range(q1 * 10, q2 * 10 + 1)]

A = set()

for x in [i / 10 for i in range(10, 600+1)]:
    if not (f(x, A) and g(x, A)):
        A.add(x)

print(sorted(A))

# Ответ: 25
