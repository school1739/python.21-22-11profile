# #3
# with open(r'web.txt') as F:
#     s = F.read()
#     c = 0
#     mx = 0
#     for i in range(len(s)):
#         if s[i] == 'E':
#             c += 1
#         else:
#             mx = max(mx, c)
#             c = 0
#     print(mx)
# Ответ: 7

# #5
with open(r'web5.txt') as F:
    s = F.read()
    strs = []

    c = 1
    mx = 0
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            c += 1
        else:
            mx = max(mx, c)
            strs.append((s[i], mx))
            c = 1
            # mx = 0

    maxLen = strs[len(strs) - 1][1]
    filtered = list(filter(lambda st: st[1] == maxLen, strs))
    print(filtered[0], filtered[len(filtered) - 1])
