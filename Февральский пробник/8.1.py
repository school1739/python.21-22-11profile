i = "0123456"
k = 0
for a in i:
    for b in i:
        for c in i:
            for d in i:
                for e in i:
                    for f in i:
                        for g in i:
                            num = a + b + c + d + e + f + g
                            if a != '0' and a != '3' and a != '5':
                                if (num.count('22') >= 1 and num.count('44') == 0) or (num.count('44') >= 1 and num.count('22') == 0) or (num.count('22') == 0 and num.count('44') == 0):
                                    k += 1
print(k)
