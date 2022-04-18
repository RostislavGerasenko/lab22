import random
import pprint

m = int(input("The number of rows in the matrix: "))
n = int(input("The number of columns in the matrix: "))
matrix = [[random.randint(1, 99) for _ in range(n)] for _ in range(m)]
print("The generated matrix:")
pprint.pp(matrix)

for row_up, row_down in zip(matrix, matrix[m//2:]):
    row_up[:n//2], row_down[n//2:] = row_down[n//2:], row_up[:n//2]

print("Transformed matrix:")
pprint.pp(matrix)
