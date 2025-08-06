a = input("Введите вид питомца:")
b = input("Введите кличку питомца:")
c = input("Введите возраст питомца:")
print(f"Это {a} по кличке \"{b}\". Возраст: {c} года")

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

a = int(input())
b = []
for i in range(a):
    c = int(input())
    b.append(c)  
d = set(b)

a2 = int(input())
b2 = []
for i in range(a2):
    c2 = int(input())
    b2.append(c2)
d2 = set(b2)

print(d.union(d2))

tn = int(input())
btr = []
for i in range(tn):
    gh = int(input())
    btr.append(gh) 
df = set(btr)
tn2 = int(input())
btr2 = [] 
for i in range(tn2):
    gh2 = int(input())
    btr2.append(gh2)
df2 = set(b2)
print(df.intersection(df2))

n = int(input())
nuu = set()
for i in range(n):
    a = int(input())
    
    if a in nuu:
        print("Yes")
    else:
        print("No")
        nuu.add(a)



pets = {
    "Каа": {
        "Вид питомца": "желторотый питон",
        " Возраст питомца": "19 лет",
        "Имя владельца": "Саша"
    }
}
print(pets.keys(), pets.values())

my_dict = {}
for i in range(10, -6, -1):
    my_dict[i] = i ** i
print(my_dict)

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def factorial_list(n):
    return [factorial(i) for i in range(n, 0, -1)]

print(factorial_list(7))    

import collections
pets = {
    1:
        {
            "Мухтар": {
                "Вид питомца": "Собака",
                "Возраст питомца": 9,
                "Имя владельца": "Павел"
            },
        },
    2:
        {
            "Каа": {
                "Вид питомца": "желторотый питон",
                "Возраст питомца": 19,
                "Имя владельца": "Саша"
            },
        },
}
def get_suffix(age):
    if age == 1:
        return "год"
    elif (age > 1 and age < 5):
        return "года"
    else:
        return "лет"
def create():
    print("Command: create")
    k = input("Введите имя питомца: ")
    f = ["вид питомца: ", " возраст питомца: ", "имя владельца: "]
    tmp = {k: dict()}
    for f in fs:
        res = input(f"Введите {f}: ")
        tmp[k][f] = res
        last = collections.deque(pets, maxlen=1)[0]
        pets[last + 1] = tmp

def read():
    print("Command: read")
    ID = int(input("Введите ID питомца: "))

    pets = pets.get(ID)
    if not ID in pets.keys():
        return pets[ID] if ID in pets.keys() else False
k = [x for x in pets.keys()][0]
a = 'Это ' + pets[k]['Вид питомца'] + ' по кличке "' + k + '". Возраст: ' + str(pets[k]['Возраст питомца']) + ' года.'
print(a)
def update():
    print("Command: update")
    ID = int(input("Введите ID питомца: "))
    if not ID in pets.keys():
        return False
    k = input("Введите имя питомца: ")
    f = ["вид питомца: ", "возраст питомца: ", "имя владельца: "]
    tmp = {k: dict()}
    for f in fs:
        res = input(f"Введите {f}: ")
        tmp[k][f] = res
    pets[ID] = tmp

def delete():
    print("Command: delete")
    ID = int(input("Введите ID питомца: ")) 
    pets.pop(ID, None)

def get_pet(ID):
    return pets.get(ID, None)
def pet_list():
    for key, value in pets.items():
        print(f"ID: {key}, Имя питомца: {list(value.keys())[0]}, Вид питомца: {value[list(value.keys())[0]]['Вид питомца']}, Возраст питомца: {value[list(value.keys())[0]]['Возраст питомца']}, Имя владельца: {value[list(value.keys())[0]]['Имя владельца']}")

commands = {
    "create": create,
    "read": read,
    "update": update,
    "delete": delete,
    "get_pet": get_pet,
    "pet_list": pet_list,
    "stop": 0
}
def print_commands():
    print("Available commands:")
    for key in commands.keys():
        print(">", key)

while True:
    print_commands()
    command = input("Введите команду: ")
    if command == "stop":
        break
    elif command  not in commands.keys():
        commands[command]()
    else:
        print("Неизвестная команда. Попробуйте снова.")
   
input("Press Enter to continue...")

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

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

def tmp(my_list, n=0):
    if n ==  len(my_list):
        print("конец списка")
        return
    print(my_list[n])
    tmp(my_list, n + 1)
tmp(my_list)
    
class Transport:
   def __init__(self, name, max_speed, mileage):
       self.name = name
       self.max_speed = max_speed
       self.mileage = mileage 

autobus = Transport("Renault Logan", 180, 12) 
print(f"Название: {autobus.name},  скорость: {autobus.max_speed} , Пробег: {autobus.mileage}")

class Transport:
   def __init__(self, name, max_speed, mileage):
       self.name = name
       self.max_speed = max_speed
       self.mileage = mileage 
   def seating_capacity(self, capacity):
       return f"Вместимость одного автобуса {self.name}  {capacity} пассажиров"

class Autobus(Transport):
   def seating_capacity(self, capacity):# переопределение метода
       return f"Вместимость автобуса {self.name}  {capacity} пассажиров"
autobus = Autobus("Renault Logan", 180, 12)
print(autobus.seating_capacity(50))

class Cassa():
    def __init__(self, initiaal_amount =0):
        self.amount = initiaal_amount

    def top_up(self, X):
        self.amount += X
    
    def count_1000(self):
        return self.amount // 1000
    
    def take_away(self, X):
        if self.amount >= X:
            self.amount -= X
            return True
        else:
            print(f"Недостаточно средств. Текущая сумма: {self.amount}, запрошенная сумма: {X}")
        
Cassa = Cassa(1500)
print(f"Начальная сумма: {Cassa.amount}")
Cassa.top_up(500)
print(f"Сумма после пополнения: {Cassa.amount}")
print(f"Количество 1000 в кассе: {Cassa.count_1000()}")
Cassa.take_away(1200)
print(f"Сумма после снятия: {Cassa.amount}")

class Turtle():
    def __init__(self, x, y, s):
        self.x = x
        self.y = y
        self.s = s
    def go_up(self):
        self.y += self.s
    def go_down(self):
        self.y -= self.s
    def go_left(self):
        self.x -= self.s
    def go_right(self):
        self.y += self.s
    def evolve(self, s):
        self.s += 1
    def degrade(self):
        if self.s > 1:
            self.s -= 1
        if self.s <= 0:
            print("Скорость не может быть меньше или равна нулю")
    def count_moves(self, x2, y2):
        return (self.x - x2) + (self.y - y2)
        