def win1(x, s):
    return x + s < 84 and (x + 3 + s >= 84 or x + s + s >= 84 or x + x + s >= 84)


def loss1(x, s):
    return not win1(x, s) and \
        win1(x + 3, s) and win1(x, s + 3) and \
        win1(x + s, s) and win1(x, s + x)


def win2(x, s):
    return loss1(x + 3, s) or loss1(x, s + 3) or \
        loss1(x + s, s) or loss1(x, s + x)


x = 12
for s in range(1, 72):
    if win1(x + 3, s) or win1(x, s + 3) or \
            win1(x + s, s) or win1(x, s + x):
        print('19:', s)
        break

# 20 & 21
s20 = []
s21 = []
for s in range(1, 190):
    if win2(x, s):
        s20.append(s)
    # Проверка на условие + проверка на подвох
    if (win1(x + 3, s) or win2(x + 3, s)) and \
        (win1(x, s + 3) or win2(x, s + 3)) and \
        (win1(x + s, s) or win2(x + s, s)) and \
        (win1(x, s + x) or win2(x, s + x)) and \
            (win1(x + 3, s) or win1(x, s + 3) or win1(x + s, s) or win1(x, s + x)) and \
            (win2(x + 3, s) or win2(x, s + 4) or win2(x + s, s) or win2(x, s + x)):
        s21.append(s)

print('20: ', min(s20), max(s20), sep='')
print('21:', min(s21))
