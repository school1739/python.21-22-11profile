with open(
    "/home/sv-cheats-1/Documents/PROJECTS/python.21-22-11profile/bundles/1/26/26.txt"
) as F:
    f = F.readlines()
    f.pop(0)
    f = list(map(lambda i: list(map(int, i.split(" "))), f))
    start = 1634305600
    end = 1634305600 + 604800

    timeUpdateProc = [0] * 604800

    c = 0
    for i in f:
        started, ended = i
        if started < start and (ended > start or ended == 0):
            c += 1
        if start <= started <= end:
            timeUpdateProc[started - start] += 1
        if start <= ended <= end:
            timeUpdateProc[ended - start] -= 1

    maxSyncronWorkingProc = 0
    cSec = 0
    for i in timeUpdateProc:
        c += i
        if c > maxSyncronWorkingProc:
            maxSyncronWorkingProc = c
            cSec = 0
        if c == maxSyncronWorkingProc:
            cSec += 1

    print(maxSyncronWorkingProc, cSec)
