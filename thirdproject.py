# https://github.com/aneka400/Links.git
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
