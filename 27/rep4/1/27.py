with open('B.txt') as F:
    f = list(map(int, F.readlines()))
    f.pop(0)

    remainders = [0] * 12

    for x in f:
        remainders[x % 12] += 1

    print(
        remainders[1]*remainders[11] +
        remainders[2]*remainders[10] +
        remainders[3]*remainders[9] +
        remainders[4]*remainders[8] +
        remainders[5]*remainders[7] +
        remainders[6]*(remainders[6]-1) / 2 +
        remainders[0]*(remainders[0]-1) / 2
    )

# Ответ: 13 149985985
