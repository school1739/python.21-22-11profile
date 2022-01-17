from time import time

# Версия 1
print('Версия 1')
start = time()
# Идем только по четным, так как у нечетных чисел нет четных делителей
for i in range(1000000, 1100000 + 1, 2):
    nums = []
    for j in range(1, int(i**0.5) + 1):
        if i % j == 0:
            nums.append(j)
            nums.append(i//j)

    # Проверяем кол-во четных делителей. Нечетных может быть сколько угодно.
    c = 0
    nums = list(set(nums))
    nums.sort()
    for n in nums:
        if n % 2 == 0:
            c += 1
    if c == 3:
        print(i, nums[-2])
end = time()
print(f'Время исполнения: {end-start}c')
# Ответ
# 1005362 502681
# 1033922 516961
# 1057058 528529
# 1074578 537289
# 1092242 546121

# Версия 2
start = time()
print('\nВерсия 2 (оптимальней по памяти)')
# Идем только по четным, так как у нечетных чисел нет четных делителей
for i in range(1000000, 1100000 + 1, 2):
    evenDivCount = 0
    for j in range(1, int(i**0.5) + 1):
        if j * j == i and j % 2 == 0:
            evenDivCount += 1
            continue
        if i % j == 0:
            if j % 2 == 0:
                evenDivCount += 1
            if i//j % 2 == 0:
                evenDivCount += 1
    if evenDivCount == 3:
        print(i, i//2)
end = time()
print(f'Время исполнения: {end-start}c')
# Ответ
# 1005362 502681
# 1033922 516961
# 1057058 528529
# 1074578 537289
# 1092242 546121
