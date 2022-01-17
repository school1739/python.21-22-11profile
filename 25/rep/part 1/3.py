for i in range(13245, 15289+1):
    nums = []
    for j in range(2, int(i**(0.5)) + 1):  # Идем от i до корня i для оптимизации
        if i % j == 0:
            nums.append(j)
            nums.append(i//j)
    if len(set(nums)) == 20:
        print(i, max(nums))

# Ответ: 13312 6656
