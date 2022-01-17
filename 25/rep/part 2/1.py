goodNums = []
for i in range(3120340, 3120452):
    # for i in range(15, 24):
    totalDivMoreThanOne = False
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            totalDivMoreThanOne = True
        if totalDivMoreThanOne:
            break
    else:
        goodNums.append(i)

for i in range(len(goodNums)):
    print(i + 1, goodNums[i])

# Ответ
# 1 3120373
# 2 3120407
# 3 3120413
# 4 3120437
# 5 3120443
