def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(value)
        matrix.append(row)
    return matrix

n = int(input('Строки: '))
m = int(input('Столбцы: '))
value = int(input('Значение: '))
result = get_matrix(n, m, value)
print(result)




