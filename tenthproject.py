# https://github.com/aneka400/Links.git
import random
r = int(input())
c = int(input())
matrix_1 = [[random.randint(1, 999) for i in range(c)] for j in range(r)]
for row in matrix_1:
    print(row)

x = int(input())
y = int(input())
matrix_2 = [[random.randint(1, 999) for i in range(y)] for j in range(x)]
for row in matrix_2:
    print(row)
matrix_3 = [[0 for j in range(y)] for i in range(x)]
for i in range(x):
    for j in range(y):
        matrix_3[i][j] = matrix_1[i][j] + matrix_2[i][j]
for row in matrix_3:
    print(row)
