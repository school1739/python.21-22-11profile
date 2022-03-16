# https://inf-ege.sdamgia.ru/problem?id=27841
# https://inf-ege.sdamgia.ru/problem?id=27842
# https://inf-ege.sdamgia.ru/problem?id=27843

def win1(s):
    return s + 1 >= 28 or s + 3 >= 28 or s * 2 >= 28


def loss1(s):
    return not win1(s) and \
        win1(s + 1) and win1(s + 3) and win1(s * 2)


def win2(s):
    return loss1(s + 1) or loss1(s + 3) or loss1(s * 2)


for s in range(1, 28):
    if win1(s + 1) or win1(s + 3) or win1(s * 2):
        print('19:', s)
        break

for s in range(1, 28):
    if win2(s):
        print('20:', s)
        # break

for s in range(1, 28):
    if (win1(s + 1) or win2(s + 1)) and \
        (win1(s + 3) or win2(s + 3)) and \
            (win1(s * 2) or win2(s * 2)):
        print('21:', s)
        break

# Ответы: 7 1012 9
