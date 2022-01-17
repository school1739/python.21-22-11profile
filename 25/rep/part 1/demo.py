for i in range(4234679, 10157813):
    nums = set()

    if int(i**0.5)**2 == i:
        for j in range(2, int(i**0.5)+1):
            if i % j == 0:
                nums.add(j)
                nums.add(i//j)
            if len(nums) > 3:
                break

        if len(nums) == 3:
            print(m, n)
