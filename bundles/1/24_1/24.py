with open("24.txt") as F:
    maxLen = 0
    f = F.readline().split("P")
    for i in f:
        if i.count("H") >= 3:
            maxLen = max(maxLen, len(i))

    print(maxLen)

# Ответ: 256
