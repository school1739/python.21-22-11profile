with open('24.txt') as F:
    s = F.readline()

    currentLen = 0
    maxLen = 0
    start = s[0]
    for i in range(1, len(s) - 1):

        if s[i] == s[i+1]:
            currentLen += 1
        else:
            if start != s[i + 1] and start != s[i]:
                maxLen = max(currentLen, maxLen)
            start = s[i]
            currentLen = 0

    print(maxLen)
