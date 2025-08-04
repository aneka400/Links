# https://github.com/aneka400/Links.git
N = int(input())
for i in range(N):
    print(i + 1, end=" ")

a = 0 
X = int(input())
for i in range(X):
    print(i + 1, end=" ")
    if i % 2 == 0:
         a += 1
print(a) 

A = int(input())
B = int(input())
for i in range(A, B + 1):
    if i % 2 == 0:
        print(i, end=" ")
