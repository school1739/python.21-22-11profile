with open("24.txt") as F:
    maxLen = 0
    f = F.readline().split("F")
    for i in f:
        if i.count("L") <= 5:
            maxLen = max(maxLen, len(i))
    print(maxLen)

# Ответ: 249
