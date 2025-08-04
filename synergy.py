a = input("Введите вид питомца:")
b = input("Введите кличку питомца:")
c = input("Введите возраст питомца:")
print("Это {a} по кличке \"{b}\". Возраст: {c} года")

print("введите этапы человека:")
a = input("Введите этап 1:")
b = input("Введите этап 2:") 
c = input("Введите этап 3:")
d = input("Введите этап 4:")
f = input("Введите этап 5:")
d = input("Введите этап 6:") 
print(a,b,c,d,f,d,sep="-")


a = int(input("1 сторона прямоугольника:"))
b = int(input("2 сторона прямоугольника:"))
c = 2 * (a + b)
d = a * b
print("Периметр прямоугольника:", c , "Площадь прямоугольника:", d )

A = 7 
B = 5
C = 2
CD = 4
F = 6
f = A ** 5
d = f * C
g = d / (CD - F)
print(g)

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


