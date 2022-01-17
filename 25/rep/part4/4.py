c = 0
n = 200_000_001

while c != 5:
    nums = []
    for i in range(2, int(n**0.5) + 1):
        if i * i == n:
            nums.append(i)
        if n % i == 0:
            nums.append(i)
            nums.append(n // i)

    nums.sort()
    M = 1
    for x in nums[:5]:
        M *= x

    if n > M and M > 0:
        print(M)
        c += 1
    n += 1
# Ответ
# 1728
# 21632
# 1260
# 1152
# 4127787
