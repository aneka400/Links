# https://github.com/aneka400/Links.git
N = int(input())
b = []
for i in range(N):
    a = int(input())
    b.append(a)
    if a == 105:
        print("error")
for i in range(N - 1, -1, -1):
    print(b[i], end=" ")

n = int(input())
b = []
for i in range(n):
    a = int(input())
    b.append(a)
print(b[: : -1])

m = int(input("масса выдержки лодки:"))
n = int(input("количество рыбаков:"))
A = []
for i in range(n):
    A.append(int(input("введите массу рыбака:")))
a = 0 
left = 0 
right = n - 1
while left <= right:
    if A[left] + A[right] <= m:
        a += 1
        left += 1
        right -= 1
    else:
        a += 1
        right -= 1
print(a)
