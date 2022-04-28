# https://inf-ege.sdamgia.ru/problem?id=13414

P = (1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21)
Q = (3, 6, 9, 12, 15, 18, 21, 24, 27, 30)
A = []

# ((x ∈ P) → (x ∈ A)) ∨ (¬(x ∈ A) → ¬(x ∈ Q))
x = 0
for x in range(1000):
    # if not(((x in P) <= (x in A)) or ((x not in A) <=  (x not in Q))):
    if not ((not (x in P) or (x in A)) or ((x in A) or not (x in Q))):
        A.append(x)
print(A)
