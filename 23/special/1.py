# https://inf-ege.sdamgia.ru/problem?id=3662
# Антон гений
s = set()

for i in range(26):
    if 3 + 3 * i - 2 * (25 - i) > 0:
        s.add(3 + 3 * i - 2 * (25 - i))
print(len(s))
