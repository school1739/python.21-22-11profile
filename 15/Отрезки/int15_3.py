# coding=UTF8

# Р = [3, 38] и Q = [21, 57]
# ((х ∈ Q) → (х ∈ Р)) → ¬(х ∈ A)
# len(A) = max
# https://inf-ege.sdamgia.ru/problem?id=34541

def f(x, A):
    return ((x in Q) <= (x in P)) <= (not (x in A))


p1, p2, q1, q2 = 3, 38, 21, 57
P = [i / 10 for i in range(p1 * 10, p2 * 10 + 1)]
Q = [i / 10 for i in range(q1 * 10, q2 * 10 + 1)]

A = set([i / 10 for i in range(10, 600 + 1)])

for x in ([i / 10 for i in range(10, 600 + 1)]):
    if not f(x, A):
        A.remove(x)

print(sorted(A))

# Ответ: A = (38, 57] => 19
