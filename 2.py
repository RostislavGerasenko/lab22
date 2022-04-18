import random
import pprint

m = int(input("The number of rows in the matrix: "))
n = int(input("The number of columns in the matrix: "))
matrix = [[random.randint(1, 99) for _ in range(n)] for _ in range(m)]
print("The generated matrix:")
pprint.pp(matrix)

#transposing the matrix so it's easier to swap
transposed = list(map(list, zip(*matrix)))

#using clever sorting trick by passing a key to sort by
min_row = transposed.index(min(transposed, key=min))
max_row = transposed.index(max(transposed, key=max))
transposed[min_row], transposed[max_row] = transposed[max_row], transposed[min_row]

matrix = list(map(list, zip(*transposed)))

print("Transformed matrix:")
pprint.pp(matrix)
