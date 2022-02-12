def win1(s):
    return s + 3 >= 95 or s * 2 >= 95


def loss1(s):
    return not win1(s) and win1(s + 3) and win1(s * 2)


def win2(s):
    return loss1(s + 3) or loss1(s * 2)


# 19
for s in range(1, 94):
    if win1(s + 3) or win1(s * 2):
        print('19:', s)
        break

# 20 & 21
answ_20 = []
answ_21 = []
for s in range(1, 94):
    # 20
    if win2(s):
        answ_20.append(s)
    if (win1(s + 3) and win2(s * 2)) or (win1(s * 2) and win2(s + 3)):
        answ_21.append(s)

print('20: ', min(answ_20), max(answ_20), sep='')
print('21:', min(answ_21))
