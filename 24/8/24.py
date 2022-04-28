# Текстовый файл 24_02.txt содержит строку из заглавных букв А, В, С, D, Е, F
# всего не более чем из 10 ^ 6 символов. Определите, сколько встречается комбинаций вида BА*АB, где
# на месте "*" может стоять любая буква, кроме А, D и
# F. В ответе укажите сначала заглавную латинскую букву, которая реже всего
# встречается на месте "*", затем общее количество подходящих комбинаций.

with open('/home/sv-cheats-1/Documents/PROJECTS/python-school/24/8/24.txt') as F:
    f = F.readline()
    m = {
        # 'A': 0,
        'B': 0,
        'C': 0,
        # 'D': 0,
        'E': 0,
        # 'F': 0
    }

    for i in range(len(f) - 4):
        l = f[i:i + 5][2]
        p1 = f[i: i + 2]
        p2 = f[i + 3: i + 5]
        if p1 == 'BA' and p2 == 'AB' and l != 'A' and l != 'D' and l != 'F':
            m[l] += 1

    print(m)
# Ответ: E398