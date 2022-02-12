def win1(s):
    return s + 1 >= 147 or s * 5 - 1 >= 147


def loss1(s):
    return not win1(s) and win1(s + 1) and win1(s * 5 - 1)


def win2(s):
    return loss1(s + 1) or loss1(s * 5 - 1)


for s in range(1, 147):
    if win1(s + 1) or win1(s * 5 - 1):
        print('19:', s)
        break

answ_20 = []
answ_21 = []
for s in range(1, 147):
    if win2(s):
        answ_20.append(s)
    if (win1(s + 1) and win2(s * 5 - 1)) or (win1(s * 5 - 1) and win2(s + 1)):
        answ_21.append(s)

print('20: ', min(answ_20), max(answ_20), sep='')
print('21:', min(answ_21))
