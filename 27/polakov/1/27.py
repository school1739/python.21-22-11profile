# https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=4411

with open('27A.txt') as F:
    n = F.readline()

    f = list(map(int, F.readlines()))

    c = 0
    for i in range(len(f) - 1):
        for j in range(i + 1, len(f)):
            sub = f[i:j+1]

            if len(sub) >= 3:
                if (sub[0] + sub[-1]) % 3 == 0 and sum(sub[1:-1]) % 2 == 0:
                    c += 1

    print(c)
