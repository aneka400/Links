#https://github.com/aneka400/Links.git
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
