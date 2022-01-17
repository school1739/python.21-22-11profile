with open(r'4.txt') as F:
    s = F.read()
    c = 0
    mx = 0
    even = '2468'
    for i in range(len(s)):
        if s[i] in even:
            c += 1
        else:
            mx = max(mx, c)
            c = 0
            
    print(mx)
