with open("24.txt") as F:
    f = F.readline().split(" ")

    print(len(max(f, key=len)))

# Ответ: 298 (ошибка в ответах 100%)
