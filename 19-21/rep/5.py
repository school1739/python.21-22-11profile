def win1(x, s):
    return x + s < 51 and ((x + s + 4) >= 51 or (2*x + s) >= 51 or (x + 2*s) >= 51)


def loss1(x, s):
    return not win1(x, s) and win1(x + 4, s) and win1(2*x, s) \
        and win1(x, s + 4) and win1(x, 2*s)


def win2(x, s):
    return loss1(x + 4, s) or loss1(2*x, s) \
        or loss1(x, s + 4) or loss1(x, 2*s)


for s in range(1, 46):
    if win1(5, s):
        print('19:', s)
        break

answ_20 = []
answ_21 = []
for s in range(1, 46):
    if win2(5, s):
        answ_20.append(s)
    if (win1(5 + 4, s) or win2(5 + 4, s)) and \
            (win1(5 * 2, s) or win2(5 * 2, s)) and \
            (win1(5, s + 4) or win2(5, s + 4)) and \
            (win1(5, s * 2) or win2(5, s * 2)):
        answ_21.append(s)

print('20:', max(answ_20))
print('21:', min(answ_21))
