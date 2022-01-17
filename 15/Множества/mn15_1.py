# P = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}, Q = {3, 6, 9, 12, 15, 18, 21, 24, 27, 30}
# ((x ∈ A) → (x ∈ P)) ∧ ((x ∈ Q) → ¬(x ∈ A))
# len(A) - max

# https://inf-ege.sdamgia.ru/problem?id=7929
P = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
Q = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]


def f(x, A):
    return ((x in A) <= (x in P)) and ((x in Q) <= (x not in A))


A = set(range(1, 41))
for x in range(1, 41):
    if not f(x, A):
        A.remove(x)

print(len(A))
# Ответ: 7
