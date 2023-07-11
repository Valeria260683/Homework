"""Создать два класса Human с атрибутами mail, age и akkount.
Akkount - это количество денег на его счету и реализовать
в этом классе метод, в котором он предоставляет информацию о себе.
Второй класс это House. Атрибутами класса House будут price,
square, а методом для класса House будет предоставление скидки.
Также необходимо реализовать несколько функций,
которые проанализируют существующие дома, тоесть экземпляры
класса House и подберут лучший вариант для определенного
экземпляра класса Human. Эту программу нужно сделать
внутри виртуального окружения."""


class Human:
    def __init__(self, mail, age, akkount):
        self.mail = mail
        self.age = age
        self.akkount = akkount

    def get_info(self):
        return f"Mail: {self.mail}, Age: {self.age}, Akkount: {self.akkount}"


class House:
    def __init__(self, price, square):
        self.price = price
        self.square = square

    def apply_discount(self, discount):
        if 0 < discount < 1:
            self.price -= self.price * discount


def analyze_homes(human):
    homes = [
        House(100000, 100),
        House(150000, 120),
        House(200000, 150)
    ]
    affordable_homes = [home for home in homes if home.price <= human.akkount]
    return affordable_homes


def select_best_home(human):
    affordable_homes = analyze_homes(human)
    if affordable_homes:
        best_home = min(affordable_homes, key=lambda home: home.square)
        return best_home
    return None

# Пример использования классов и функций
human1 = Human("example1@mail.com", 30, 200000)
print(human1.get_info())  # Mail: example1@mail.com, Age: 30, Akkount: 200000

home1 = House(100000, 100)
print(home1.price)  # 100000

home1.apply_discount(0.1)
print(home1.price)  # 90000

affordable_homes = analyze_homes(human1)
for home in affordable_homes:
    print(home.price, home.square)
# Output:
# 100000 100
# 150000 120
# 200000 150

best_home = select_best_home(human1)
print(best_home.price, best_home.square)
# Output:
# 100000 100
