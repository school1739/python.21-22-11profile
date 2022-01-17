c = 0
n = 600001
while c != 5:
    nums = []
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            if i % 10 == 7 and i != 7 and i != n:
                nums.append(i)
            ni = n//i
            if ni % 10 == 7 and ni != 7 and ni != n:
                nums.append(ni)
    nums = list(set(nums))
    nums.sort()

    if nums:
        print(n, nums[0])
        c += 1

    n += 1
# Ответ
# 600001 437
# 600002 47
# 600003 1227
# 600005 217
# 600012 16667
