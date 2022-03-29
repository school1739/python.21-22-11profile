# https://inf-ege.sdamgia.ru/problem?id=34519
A = 1

while True:
    for x in range(1000):
        if not(
            (x & 9 == 0) <= ((x & 19 != 0) <= (x & A != 0))
        ):
            break
    else:
        print(A)
        break

    A += 1
