# 4. DataClass:
#   - Создайте файл "student_dataclass.py" для написания кода с использованием DataClass.
#   - Импортируйте dataclass из модуля dataclasses.
#  - Определите DataClass для представления данных о студентах.

from typing import List
from dataclasses import dataclass

@dataclass
class Student:
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
