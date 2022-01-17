f = open('17.txt')

a = [int(i) for i in f]

c = 0
mx = -1

for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if (a[i] + a[j]) % 9 == 0:
            c += 1
            mx = max(a[i] + a[j], mx)

print(c, mx)
