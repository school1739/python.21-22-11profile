def Win(x):
    return ((x < 64) and ((x+4 >= 64) or ((x*2)-2 >= 64)))


def Loss(x):
    return ((not Win(x)) and (Win(x+4) and Win((x*2)-2)))


def NS(x):
    return (not Win(x) and (Loss(x+4) or Loss((x*2)-2)))


N21 = []
not_N21 = []

for x in range(1, 63+1):
    if NS(x+4) and NS((x*2)-2):
        not_N21.append(x)
    if Win(x+4) and Win((x*2)-2):
        not_N21.append(x)
    if (Win(x+4) or NS(x+4)) and (Win((x*2)-2) or NS((x*2)-2)):
        if not(x in not_N21):
            N21.append(x)
print(min(N21))
