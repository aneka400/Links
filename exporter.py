def my_print():
    """
        Тело функции
    """
#print("Hello, World!")

def my_sum(a, b):
    return a + b
#print(my_sum(3))

def my_sum2(a, b=5):
    return a + b
#print(my_sum2(3, 7))

def my_print2(print_string="Hello, World!"):
    print(print_string)
#my_print2("asdasd")

def hello_str(): return "Hello"
def bye_str(): return "Bye"

def my_print_from_func(func):
    print(func())
#print(hello_str())
#my_print_from_func(hello_str)
#my_print_from_func(bye_str)
#my_print_from_func("asdasd")

def my_print_from_func_2(func):
    if callable(func): print(func())
    else: print("func is not callable")
#my_print_from_func_2(hello_str)
#my_print_from_func_2(bye_str)
#my_print_from_func_2("asdasd")
"""
from abc import abstractmethod
class Employee:
    def __init__(self, age, name, salary) -> None:
        self.age = age
        self.name = name
        self.salary = salary
    
    @abstractmethod
    def get_salary(self):
        raise NotImplementedError('Metod not implemented')

class Programmer(Employee):
    def __init__(self, age, name, salary) -> None:
        super().__init__(age, name, salary)

    def get_salary(self):
        return self.salary 

class Manager(Employee):
    def __init__(self, age, name, salary) -> None:
        super().__init__(age, name, salary) 
    def get_salary(self):
        return self.salary() * 1.3

if __name__ == '__main__':
    programmer = Programmer(30, 'Владимир', 100_000)
    print(programmer.name, programmer.salary, programmer.get_salary())

    #manager = Manager(20, 'Алексей', 120_000)
    #print(manager.name, manager.salary, manager.get_salary())
"""
"""Не правильно"""
class User:
    def __init__(self, name: str) -> None:
        self.name = name

    def get_name(self) -> str:
        pass 

    def save(self,user):
        pass

""" Правильно """
class User:
    def __init__(self, name: str) -> None:
            self.name = name

    def get_name(self):
        return self

class UserDB:
    def get_user(self, id) -> User:
        """ 
            Запрос в базу
        """
        pass

def save(self, user:User):
    """
        Запрос в базу
    """
    pass


"""Не правильно"""
class Discount:
    def __init__(self, customer, price):
        self.customer = customer
        self.price = price 
    
    def give_discount(self):
        if self.customer == 'fav':
            return self.price * 0.2
        if self.customer == 'vip':
            return self.price * 0,4

"""Правильно"""
class Discount:
    def __init__(self, customer, price):
        self.customer = customer
        self.price = price
    
    def get_discount(self):
        return self.price * 0,2
    
class VipDiscount(Discount):
    def get_discount(self):
        return super().get_discount() * 2
    
class SuperVipDiscount(Discount):
    def get_discount(self):
        return super().get_discount() * 4

"""Не правильно"""
class Employee:
    def __init__(self, data) -> None:
        self.age = data[0]
        self.name = data[1]
        self.salary = data[2]
    
    def get_salary(self, salary):
        self.salary = salary

class Accountant(Employee):
    def __init__(self, data) -> None:
        super().__init__(data)

    def set_coef(self, coef):
        self.coef = coef

"""Правильно"""
class Employee(Employee):
    def __init__(self, age, name, salary) -> None:
        self.age = age
        self.name = name
        self.salary = salary
    
    def set_salary(self, salary):
        self.salary = salary

    def set_coef(self, coef):
        self.coef = coef

class Accountatnt:
    def __init__(self, age, name, salary, coef) -> None:
        super().__init__(age, name, salary)
    
    def set_coef(self, coef = 0.5):
        self.coef = coef 

"""Не правильно"""
class Creature:
    def __init__(self, age) -> None:
        self.age = age 
    
    def run(self):
        pass

    def swim(self):
        pass

    def speak(self):
        pass

class Human(Creature):
    ...

class Cat(Creature):
    ...

"""Правильно"""
class Creature:
    def __init__(self, age) -> None:
        self.age = age
    
class RunInterface:
    def run(self):
        pass

class SwimInterface:
    def swim(self):
        pass

class SpeakInterface:
    def speak(self):
        pass

class Human(Creature, RunInterface, SwimInterface, SpeakInterface):
    ...

class Cat(Creature, RunInterface, SpeakInterface):
    ...

if __name__ == '__main__':
    cat = Cat(5)
    cat.speak()

"""Не правильно"""
class ElkLogging:
    def log(str):
        print(str)

class ConsoleLogging:
    def log(str):
        print(str)

class Logger():

    def __init__(self) -> None:
        self.elk = ElkLogging()
        self.console = ConsoleLogging()
    
    def elk_log(self, log):
        self.elk.logging.log(log)
    
    def console_log(self, log):
        self.console.logging.log(log)

"""Правильно"""
class ElkLogging:
    def log(self, str):
        print(str)

class ConsoleLogging:
    def log(self, str):
        print(str)

class Logger():
    def __init__(self, logging_wrapper) -> None:
        self.logging_wrapper = logging_wrapper
        def log(self, log):
            self.logging_wrapper.log(log)

if __name__ == '__main__':
    logger = Logger(ConsoleLogging)
    #logger.log("asdasd")
""""
class Foo:
    Age = None
    salary = 0
    def __init__(self, name=None) -> None:
        print("Мы в конструкторе")
        self.name = name 
        self.Motivation = 0 

    def __call__(self, a):
        print('__call__', a)
    
    def __setattr__(self, name, value):
        print(f"{name=}", f"{value=}")
        if name == 'salary':self.__dict__['Motivation'] = value * 0,5
        self.__dict__[name] = value

    def __enter__(self):
        return self.name
    
    def __exit__(self, exception_typ, exception_val, trace):
        ...
    
    def get_motivation(self):
        return self.Motivation

if __name__ == '__main__':
    foo = Foo()
    foo(5)
    foo.name = "Заполнять имя"
    foo.Age = 30
    foo.salary = 50_000
    print(foo.Motivation)
    with Foo(name='asd') as f:
        print(f)
"""

import tracemalloc
class Singleton(object):

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            print(1)
            cls.obj=range(0, 10_000_000_000)
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance
    
    def __init__(self)-> None:
        ...
    
    def foo(self):
        return "Singleton"

class NotSingleton(object):
    def __init__(self) -> None:
        self.obj=range(0, 10_000_000_000)
    
    def foo(self):
        return "NotSingleton"
    
if __name__ == '__main__':
    """
    singleton1 = Singleton()
    print(id(singleton1))
    singleton2 = Singleton()
    print(id(singleton2))

    not_singleton1 = NotSingleton()
    print(id(not_singleton1))
    not_singleton2 = NotSingleton()
    print(id(not_singleton2))
    """
    """
    tracemalloc.start()
    rs = []
    for _ in range(0,1000):
        singleton3 = Singleton()
        singleton3.foo()
    print(tracemalloc.get_traced_memory())
    tracemalloc.stop()

    tracemalloc.start()
    for _ in range(0,1000):
        not_singleton3 = NotSingleton()
        not_singleton3.foo()
    print(tracemalloc.get_traced_memory())
    tracemalloc.stop()
    """
    tracemalloc.start()
    rs = []
    for _ in range(0, 100000):
        rs.append(Singleton())
    print(tracemalloc.get_traced_memory())
    tracemalloc.stop()

    tracemalloc.start()
    rs = []
    for _ in range(0, 100000):
        rs.append(NotSingleton())
    print(tracemalloc.get_traced_memory())
    tracemalloc.stop()