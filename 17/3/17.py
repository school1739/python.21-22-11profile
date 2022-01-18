f = open('17.txt')
nums = [int(l) for l in f]

c = 0
mx = -1

for i in range(len(nums) - 1):
    for j in range(i + 1, len(nums)):
        if (nums[i] + nums[j]) % 9 == 0:
            c += 1
            mx = max(mx, nums[i] + nums[j])

print(c, mx)
