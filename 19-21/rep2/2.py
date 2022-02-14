def win1(x, s):
    return x + s < 190 and (x + 4 + s >= 190 or x * 2 + s >= 190 or x + s * 2 >= 190)


def loss1(x, s):
    return not win1(x, s) and win1(x + 4, s) and win1(x, s + 4) and win1(x * 2, s) and win1(x, s * 2)


def win2(x, s):
    return loss1(x + 4, s) or loss1(x, s + 4) or loss1(x * 2, s) or loss1(x, s * 2)


for s in range(1, 190):
    if win1(10 + 4, s) or win1(10, s + 4) or win1(10 * 2, s) or win1(10, s * 2):
        print('19:', s)
        break

# 20 & 21
s20 = []
s21 = []
for s in range(1, 190):
    if win2(10, s):
        s20.append(s)
    # Проверка на условие + проверка на подвох
    if (win1(10 + 4, s) or win2(10 + 4, s)) and \
        (win1(10, s + 4) or win2(10, s + 4)) and \
        (win1(10 * 2, s) or win2(10 * 2, s)) and \
        (win1(10, s * 2) or win2(10, s * 2)) and \
            (win1(10 + 4, s) or win1(10, s + 4) or win1(10 * 2, s) or win1(10, s * 2)) and \
            (win2(10 + 4, s) or win2(10, s + 4) or win2(10 * 2, s) or win2(10, s * 2)):
        s21.append(s)

print('20: ', min(s20), max(s20), sep='')
print('21:', max(s21))
