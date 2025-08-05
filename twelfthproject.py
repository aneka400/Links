#https://github.com/aneka400/Links.git
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
