c = 0
n = 200_000_001
while c != 5:
    nums = set()
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            nums.add(i)
        if len(nums) > 5:
            break
    m = 1
    if len(nums) == 5:
        for i in nums:
            m *= i
    else:
        m = 0

    if n > m > 0:
        c += 1
        print(m, n)
    n += 1
