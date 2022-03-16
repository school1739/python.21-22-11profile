# https://inf-ege.sdamgia.ru/problem?id=28239
# https://inf-ege.sdamgia.ru/problem?id=28240
# https://inf-ege.sdamgia.ru/problem?id=28241

def win1(s):
    return s + 1 >= 201 or s * 5 >= 201


def loss1(s):
    return not win1(s) and \
        win1(s + 1) and win1(s * 5)


def win2(s):
    return loss1(s + 1) or loss1(s * 5)


for s in range(1, 201):
    if win1(s + 1) or win1(s * 5):
        print('19:', s)
        break

for s in range(1, 201):
    if win2(s):
        print('20:', s)
        # break

for s in range(1, 201):
    if (win1(s + 1) or win2(s + 1)) and \
            (win1(s * 5) or win2(s * 5)):
        print('21:', s)
        break

# Ответы: 9 839 38
