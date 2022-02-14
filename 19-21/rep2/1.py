def win1(x, s):
    return x + s < 56 and (x + s + 2 >= 56 or x + s * 3 >= 56 or x * 3 + s >= 56)


def loss1(x, s):
    return not win1(x, s) and win1(x + 2, s) and win1(x, s + 2) and win1(x * 3, s) and win1(x, s * 3)


def win2(x, s):
    return loss1(x + 2, s) or loss1(x, s + 2) or loss1(x * 3, s) or loss1(x, s * 3)


# 19
for s in range(1, 51):
    if win1(5 + 2, s) or win1(5, s + 2) or win1(5 * 3, s) or win1(5, s * 3):
        print('19:', s)
        break


# 20 & 21
s20 = []
s21 = []
for s in range(1, 51):
    if win2(5, s):
        s20.append(s)

    if (win1(5 + 2, s) or win2(5 + 2, s)) and \
        (win1(5, s + 2) or win2(5, s + 2)) and \
        (win1(5 * 3, s) or win2(5 * 3, s)) and \
            (win1(5, s * 3) or win2(5, s * 3)):
        s21.append(s)

print('20: ', min(s20), max(s20), sep='')
print('21:', len(s21))
