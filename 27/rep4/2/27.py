with open('A.txt') as F:
    f = list(map(int, F.readlines()))
    f.pop(0)
    div10, div5, div2 = 0, 0, 0

    for x in f:
        if x % 10 == 0:
            div10 += 1
        elif x % 5 == 0:
            div5 += 1
        elif x % 2 == 0:
            div2 += 1

    print(div10 * (len(f)-div10) + div10 * (div10 - 1) / 2 + div5 * div2)

# Ответ: 25 480521685
