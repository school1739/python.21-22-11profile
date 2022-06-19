# https://inf-ege.sdamgia.ru/problem?id=35915
def binarySearch(arr, l, r, x):

    while l <= r:
        mid = l + (r - l) // 2

        # Check if x is present at mid
        if arr[mid] == x:
            return mid

        # If x is greater, ignore left half
        elif arr[mid] < x:
            l = mid + 1

        # If x is smaller, ignore right half
        else:
            r = mid - 1

    # If we reach here, then the element
    # was not present
    return -1


with open('/home/sv-cheats-1/Documents/PROJECTS/python-school/26/6/26.txt') as F:
    n = F.readline()
    f = sorted(map(int, F.readlines()))
    fFiltered = sorted(filter(lambda x: x % 2 != 0, f))
    c = avrgMax = 0
    for i in range(len(fFiltered) - 1):
        for j in range(i + 1, len(fFiltered)):
            avrg = (fFiltered[i] + fFiltered[j]) // 2
            if binarySearch(f, 0, len(f) - 1, avrg) != -1:
                c += 1
                avrgMax = max(avrg, avrgMax)
    print(c, avrgMax)
