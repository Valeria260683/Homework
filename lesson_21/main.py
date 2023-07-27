# 4. Результат решения задачи:
# После создания классов и функции с атрибутами
# и аннотациями типов данных, можно использовать
# эти классы и функции в других частях кода для
# создания экземпляров классов, вызова методов
# и получения результатов.
# Например, в файле "main.py" можно импортировать
# классы и функции и использовать их:

from classes.person import Person
from classes.car import Car
from classes.book import Book
from functions.calculate import calculate_sum

person = Person()
person.name = "John"
person.age = 25
print(person.name)
print(person.age)

car = Car()
car.brand = "Toyota"
car.model = "Camry"
car.year = 2020
print(car.brand)
print(car.model)
print(car.year)

book = Book()
book.title = "Harry Potter"
book.author = "J.K. Rowling"
book.publication_year = 1997
print(book.title)
print(book.author)
print(book.publication_year)

result = calculate_sum(5, 10)
print(result)

# В этом примере использованы явные аннотации типов данных,
# так как они являются более простыми и понятными для чтения
# и понимания кода. Однако, неявные аннотации также могут быть
# полезны, особенно при работе с большими проектами, где
# документация и подсказки могут быть важными для
# других разработчиков.