# https://inf-ege.sdamgia.ru/problem?id=28065
# https://inf-ege.sdamgia.ru/problem?id=28066
# https://inf-ege.sdamgia.ru/problem?id=28067

def win1(s):
    return s + 1 >= 39 or s + 2 >= 39 or s * 2 >= 39


def loss1(s):
    return not win1(s) and \
        win1(s + 1) and win1(s + 2) and win1(s * 2)


def win2(s):
    return loss1(s + 1) or loss1(s + 2) or loss1(s * 2)


for s in range(1, 39):
    if win1(s + 1) or win1(s + 2) or win1(s * 2):
        print('19:', s)
        break

for s in range(1, 39):
    if win2(s):
        print('20:', s)
        # break

for s in range(1, 39):
    if (win1(s + 1) or win2(s + 1)) and \
        (win1(s + 2) or win2(s + 2)) and \
            (win1(s * 2) or win2(s * 2)):
        print('21:', s)
        break

# Ответы: 10 1718 16
