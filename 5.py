import random
import pprint

m = int(input("The size of the square matrix: "))
matrix = [[random.randint(1, 99) for _ in range(m)] for _ in range(m)]
print("The generated matrix:")
pprint.pp(matrix)


# ABCD   xxxABCD
# EFGH   xxEDGHx
# IJKL   xIJKLxx
# MNOP   MNOPxxx
# After shifting matrix like so, the diagonals of original matrix become columns

shifted_matrix = [[None]*(m-i-1) + row + [None]*i for i, row in enumerate(matrix)]
for i, diagonal in enumerate(zip(*shifted_matrix), 1):
    print(f"Diagonal number {i}: {', '.join(str(element) for element in diagonal if element)}")
