import random
import pprint

m = int(input("The number of rows in the matrix: "))
n = int(input("The number of columns in the matrix: "))
matrix = [[random.randint(1, 99) for _ in range(n)] for _ in range(m)]
print("The generated matrix:")
pprint.pp(matrix)

for row in matrix:
    min_index = row.index(min(row))
    max_index = row.index(max(row))
    row[min_index], row[max_index] = row[max_index], row[min_index]

print("Transformed matrix:")
pprint.pp(matrix)
