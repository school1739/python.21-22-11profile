s = '2' * 105

while '222' in s or '555' in s:
    if '555' in s:
        s = s.replace('555', '2', 1)
    else:
        s = s.replace('2222', '5', 1)

print(s)
# Ответ: 522
