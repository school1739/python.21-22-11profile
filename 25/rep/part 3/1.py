# Версия 1
print('Версия 1')
n = 600001
c = 0
while c != 6:
    nums = []
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            nums.append(i)
            nums.append(n//i)
    nums = list(set(nums))
    if len(nums) == 0:
        F = 0
    else:
        F = max(nums) - min(nums)
    if F != 0 and F % 7 == 0:
        print(n, F)
        c += 1
    n += 1

# Ответ
# 600002 299999
# 600016 300006
# 600021 200004
# 600023 3878
# 600030 300013
# 600041 46144

print('\nВерсия 2')
# Версия 2
n = 600001
c = 0
while c != 6:
    F = 0
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            F = n//i - i
            break

    if F != 0 and F % 7 == 0:
        print(n, F)
        c += 1
    n += 1

# Ответ
# 600002 299999
# 600016 300006
# 600021 200004
# 600023 3878
# 600030 300013
# 600041 46144
