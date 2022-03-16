# https://inf-ege.sdamgia.ru/problem?id=28074
# https://inf-ege.sdamgia.ru/problem?id=28075
# https://inf-ege.sdamgia.ru/problem?id=28076

def win1(s):
    return s + 1 >= 44 or s + 2 >= 44 or s * 2 >= 44


def loss1(s):
    return not win1(s) and \
        win1(s + 1) and win1(s + 2) and win1(s * 2)


def win2(s):
    return loss1(s + 1) or loss1(s + 2) or loss1(s * 2)


for s in range(1, 44):
    if win1(s + 1) or win1(s + 2) or win1(s * 2):
        print('19:', s)
        break

for s in range(1, 44):
    if win2(s):
        print('20:', s)
        # break

for s in range(1, 44):
    if (win1(s + 1) or win2(s + 1)) and \
        (win1(s + 2) or win2(s + 2)) and \
            (win1(s * 2) or win2(s * 2)):
        print('21:', s)
        break

# Ответы: 11 1920 18
