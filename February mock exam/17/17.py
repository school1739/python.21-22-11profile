f = open("17.txt")
num = [int(x) for x in f]

c, maxSum,  maxDiv11 = 0, 0, 0
for i in num:
    if i % 11 == 0:
        maxDiv11 = max(maxDiv11, i)

for i in range(len(num) - 1):
    if num[i] + num[i + 1] <= maxDiv11 and \
            (num[i] % 11 == 0 or num[i + 1] % 11 == 0):
        c += 1
        maxSum = max(maxSum, num[i] + num[i + 1])

print(c, maxSum)
