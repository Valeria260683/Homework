"""Написать программу с классом Car, написать конструктор в ней, создать атрибуты класса Car:
цвет, тип, год. Написать 5 методов: 1ый метод - это запуск автомобиля (при его вызове будет
выводиться сообщение, что автомобиль заведен); 2 ой метод - это отключение автомобиля
(при его вызове будет выводиться сообщение, что автомобиль заглушен); 3 ий, 4 ый
и 5 ый методы будут на присвоение автомобилю цвета, типа и года.
С пояснением написать решение"""

class Car:
    def __init__(self, color, car_type, year):
        self.color = color
        self.car_type = car_type
        self.year = year

    def start(self):
        print("Автомобиль заведен")

    def stop(self):
        print("Авто заглушен")

    def set_color(self, new_color):
        self.color = new_color
        print(f"Новый цвет автомобиля: {self.color}")

    def set_type(self, new_type):
        self.car_type = new_type
        print(f"Тип автомобиля теперь: {self.car_type}")

    def set_year(self, new_year):
        self.year = new_year
        print(f"Год выпуска обновлен: {self.year}")
my_car = Car("Красный", "Седан", "2015")
my_car.start() # Автомобиль заведен
my_car.stop() # Автомобиль заглушен
my_car.set_color("Синий") # Новый цвет автомобиля: Синий
my_car.set_type("Хэтчбек") # Тип автомобиля теперь: Хэтчбек
my_car.set_year("2019") # Год выпуска обновлен: 2019
