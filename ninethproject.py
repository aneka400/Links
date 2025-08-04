# https://github.com/aneka400/Links.git
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

  
