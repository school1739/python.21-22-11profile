def isSimple(x):
    for i in range(2, int(x**0.5)):
        if x % i == 0 or x % (x//i) == 0:
            return False
    return True


n = 560001
c = 0

while c != 6:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            if isSimple(n//i):
                print(n, n//i)
                c += 1
            break
    n += 1

# Ответ
# 560002 280001
# 560003 2179
# 560009 2467
# 560011 5437
# 560013 186671
# 560018 280009
