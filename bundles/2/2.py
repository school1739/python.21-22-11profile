for i in range(26600, 28101):
    nums = set()

    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            nums.add(j)
            nums.add(i // j)

    if len(nums) > 0 and len(nums) % 13 == 0:
        print(i, len(nums))
