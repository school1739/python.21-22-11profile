def win1(s):
    if s + 5 >= 78 or s * 4 - 3 >= 78:
        return True
    return False


def loss1(s):
    if not win1(s) and win1(s + 5) and win1(s * 4 - 3):
        return True
    return False


def win2(s):
    if loss1(s + 5) or loss1(s * 4 - 3):
        return True
    return False


def loss12(s):
    if (win2(s * 4 - 3) and win1(s + 5)) or (win2(s + 5) and win1(s * 4 - 3)):
        return True
    return False


for s in range(1, 78):
    # 19
    if win1(s + 5) or win1(s * 4 - 3):
        print('19:', s)
        break

asw_20 = []
asw_21 = []
for s in range(1, 78):
    # 20
    if win2(s):
        asw_20.append(s)
    # 21
    if loss12(s):
        asw_21.append(s)
print('20: ', min(asw_20), max(asw_20), sep="")
print('21:', min(asw_21))
