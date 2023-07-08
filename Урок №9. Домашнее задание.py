"""Создать Class humen (человек). Определить у этого класса четыре динамических атрибута
и один статический. Также для этого класса необходимо создать два своих каких-то метода,
например work и еще какой-то.  Кроме этого, самому придумать два атрибута и переопределить
магический метод __ str __ и создать несколько экземпляров этого класса и вызвать
придуманные методы."""

class Human:
# статический атрибут
    species = "Homo sapiens"

    def __init__(self, name, age, gender, occupation):
    # динамические атрибуты
        self.name = name
        self.age = age
        self.gender = gender
        self.occupation = occupation

    # дополнительные атрибуты
        self.hobby = ""
        self.nationality = ""

    def work(self):
        print(f"{self.name} is working as a {self.occupation}.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

    def __str__(self):
        return f"{self.name} {self.age} years old, {self.gender}, {self.occupation}"

#создаем экземпляры класса
John = Human("John", 30,"male", "programmer" )
Jane = Human("Jane", 25, "female", "teacher")
#выводим экземпляры класса
print(John)
print(Jane)
#вызываем методы объектов
John.work()
Jane.sleep()

#задаем значения дополнительным атрибутам
John.hobby = "playing guitar"
Jane.nationality = "American"

