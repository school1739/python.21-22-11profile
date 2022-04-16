def isPrime(x):
    nums = set()
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            nums.add(i)
            nums.add(x // i)
        if len(nums) > 0:
            break
    if len(nums) > 0:
        return False
    return True


curPrimeLen = 0
s = 0
results = []
remainders = [0] + [None] * 21
sums = [0] + [None] * 21
with open('27B.txt') as F:
    for i in range(int(F.readline())):
        x = int(F.readline())

        # Проверка числа на простоту
        if isPrime(x):
            curPrimeLen += 1
        s += x

        if remainders[curPrimeLen % 22] == None:
            remainders[curPrimeLen % 22] = curPrimeLen
            sums[curPrimeLen % 22] = s
        else:
            results.append([curPrimeLen - remainders[curPrimeLen %
                           22], s - sums[curPrimeLen % 22]])
print(max(results))

# Ответ: 68768 69982103
