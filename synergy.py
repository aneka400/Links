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

a = int(input())
if a > 0:
    if a % 2 == 0:
        print("Положительное четное число")
    else:
        print("Положительное нечетное число")
elif a == 0:
    print("нулевое число")
else:
    if a % 2 == 0:
        print("Отрицательное четное число")
    else:
        print("число не является четным")

a = input("ВВедите слово из маленьких латинских букв:")
b = 0
c = 0
for  letter in a:
    if letter in "aeiou":
        b += 1
    elif letter in "bcdfghjklmnpqrstvwxyz":
        c += 1
if not b:
    print("False")
else:
        print("True")
print("Количество гласных:", b)

X = int(input("Минимальная сумма инвестиций:"))
Mike = int(input("A  долларов у Майка:"))
ivan = int(input("B долларов у Ивана:"))
if Mike >= sum and ivan >= sum:
    print(2)
elif Mike >= sum:
    print(Mike)
elif ivan >= sum:
    print(ivan)
elif  ((Mike + ivan) >= sum):
    print(1)
else:
    ((Mike + ivan) <= sum)
    print(0)