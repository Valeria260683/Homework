# В папке "classes" создадим файл "car.py" и опишем в
# нем класс "Car" с различными атрибутами:
class Car:
    def __init__(self):
        self.brand: str = ""
        self.model: str = ""
        self.year: int = 0
        self.mileage: float = 0.0
        self.is_electric: bool = False