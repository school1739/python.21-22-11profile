f = open("17.txt")
num = [int(x) for x in f]
n =[]
for i in range (0, len(num)):
    if num[i] % 11 == 0:
        n.append(num[i])
print(max(n))
