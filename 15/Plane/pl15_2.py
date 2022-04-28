# https://inf-ege.sdamgia.ru/problem?id=18824

for a in range(1, 1000):
    for x in range(1, 500):
        for y in range(1, 500):
            if not((x * y < a) or (y > x) or (x >= 8)):
                break
        else:
            continue
        break
    else:
        print(a)
        break
