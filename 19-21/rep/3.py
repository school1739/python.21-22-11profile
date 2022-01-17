def win1(n):
    if n + 1 >= 147 or n * 5 - 1 >= 147:
        return True
    return False


for s in range(1, 147):
    if win1(s + 1) or win1(s * 5 - 1):
        print('19:', s)
        break


def loss1(n):
    if not win1(n) and win1(n + 1) and win1(n * 5 + 1):
        return True
    return False


nums = set()
for s in range(1, 147):
    if loss1(s + 1) or loss1(s * 5 - 1):
        nums.add(s)

print('20: ', min(nums), max(nums), sep='')


def win12(n):
    if
