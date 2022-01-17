# https://inf-ege.sdamgia.ru/problem?id=33526
with open(r'3.txt') as F:
    s = F.read()

    # Словарь всех повторений букв
    all = {}

    
    for i in range(len(s) - 2): # Перебор
        if s[i] == s[i + 2]: # Условие
            all.update({s[i + 1]: all.get(s[i + 1], 0) + 1}) # Обновить количество повторений букв в словаре

    print(all) # Вывод словаря, смотрим ручками значение