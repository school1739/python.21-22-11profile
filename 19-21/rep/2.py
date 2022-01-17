def win1(n):
    if n + 3 >= 95 or n * 2 >= 95:
        return True
    return False


def loss1(n):
    if not win1(n) and win1(n + 3) and win1(n * 2):
        return True
    return False


def win2(n):
    if loss1(n + 3) or loss1(n * 2):
        return True
    return False


for s in range(1, 95):
    if win1(s * 2) or win1(s + 3):
        print('19:', s)
        break

for s in range(1, 95):
    if win2(s):
        print('20:', s)
