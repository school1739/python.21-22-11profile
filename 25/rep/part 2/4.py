for i in range(200100, 200131):
    nums = []
    for j in range(1, int(i**0.5) + 1):
        if i % j == 0:
            nums.append(j)
            nums.append(i//j)

    if len(set(nums)) == 4:
        print(i, nums)

# Ответ
# 200101 [1, 200101, 11, 18191]
# 200111 [1, 200111, 97, 2063]
# 200113 [1, 200113, 83, 2411]
# 200114 [1, 200114, 2, 100057]
# 200119 [1, 200119, 293, 683]
