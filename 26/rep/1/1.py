from math import floor
f = open(r'1.txt').readlines()
n, k = map(int, f.pop(0).split(' '))

nums = sorted(map(int, f))
nums = nums[k:len(nums) - k]
minimum = min(nums)
avrg = int(sum(nums) / len(nums))

print(minimum, avrg)

# Ответ: 41 501

# Другое решение
# with open("1.txt") as F:
#     n, k = map(int, F.readline().split())
#     a = []
#     for i in range(n):
#         a.append(int(F.readline())) a.sort()
#     a = a[k:-k]
#     summa = sum(a)
#     sred = int(summa/len(a))
#     print(a[0], sred)
