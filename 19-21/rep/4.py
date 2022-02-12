def win1(x, s):
    return x + s < 91 and ((x + s + 1) >= 91 or (3*x + s) >= 91 or (x + 3*s) >= 91)


def loss1(x, s):
    return not win1(x, s) and win1(x + 1, s) and win1(3*x, s) \
        and win1(x, s + 1) and win1(x, 3*s)


def win2(x, s):
    return loss1(x + 1, s) or loss1(3*x, s) \
        or loss1(x, s + 1) or loss1(x, 3*s)


for s in range(1, 85):
    if win1(14, s):
        print('19:', s)
        break

answ_20 = []
answ_21 = []
for s in range(1, 85):
    if win2(14, s):
        answ_20.append(s)
    if (win1(14 + 1, s) or win2(14 + 1, s)) and \
            (win1(14 * 3, s) or win2(14 * 3, s)) and \
            (win1(14, s + 1) or win2(14, s + 1)) and \
            (win1(14, s * 3) or win2(14, s * 3)):
        answ_21.append(s)

print('20:', max(answ_20))
print('21:', min(answ_21))
