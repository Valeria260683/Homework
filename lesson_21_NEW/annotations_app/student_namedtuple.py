# 2. NamedTuple:
# - Создайте файл "student_namedtuple.py" для написания кода с использованием NamedTuple.
# - Импортируйте NamedTuple из модуля typing.
# - Определите NamedTuple для представления данных о студентах.


from typing import NamedTuple, List

class Student(NamedTuple):
    name: str
    age: int
    average_score: float

def process_students(students: List[Student]):
    for student in students:
        print(f"Name: {student.name}, Age: {student.age}, Average Score: {student.average_score}")

students = [
    Student("Alice", 20, 4.5),
    Student("Bob", 21, 3.8),
    Student("Charlie", 19, 4.2)
]

process_students(students)