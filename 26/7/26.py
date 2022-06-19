# https://inf-ege.sdamgia.ru/problem?id=35484

def binsearch(arr, l, r, x):
    while l <= r:
        mid = l + (r - l) // 2

        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            l = mid + 1
        elif arr[mid] > x:
            r = mid - 1

    return -1


with open(r'26.txt') as F:
    f = sorted(map(int, F.readlines()))
    g = list(filter(lambda x: x % 2 == 0, f))

    c = avrgMax = 0
    for i in range(len(g) - 1):
        for j in range(i + 1, len(g)):
            avrg = (g[i] + g[j]) // 2
            if binsearch(f, 0, len(f) - 1, avrg) != -1:
                c += 1
                avrgMax = max(avrg, avrgMax)
    print(c, avrgMax)

# Ответ: 15 976339247
