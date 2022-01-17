for i in range(28521, 28562):
    nums = []
    for j in range(1, i + 1):
        if i % j == 0:
            nums.append(j)
        if len(nums) > 5:
            break
    if len(nums) == 5:
        print(nums)
