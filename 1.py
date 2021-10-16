a = [1, 1, True, False, 'True', False, [12, 3], [12, 3]]
c = 0
b = a.copy()

for i in a:
    b.remove(i)
    for z in b:
        if i is z:
            c = c + 1
d = len(a) - c
print(f'Дубликатов: {c}\nОригинальных: {d}')
