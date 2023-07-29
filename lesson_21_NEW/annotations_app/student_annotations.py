"""Задача: Рассмотрим набор данных о студентах, который содержит их имя,
 возраст и средний балл. Необходимо создать структуру данных
 для представления этих данных и написать решение с использованием
 аннотаций типов, NamedTuple, TypedDict и DataClass."""

# 1. Аннотации типов:
#  - Создайте файл "student_annotations.py" для написания кода с аннотациями типов.
#  - Используйте аннотации типов для определения структуры данных о студентах.

from typing import List


class Student:
    def __init__(self, name: str, age: int, average_score: float):
        self.name = name
        self.age = age
        self.average_score = average_score

def process_students(students: List[Student]):
    for student in students:
        print(f"Name: {student.name}, Age: {student.age}, Average Score: {student.average_score}")


students = [
    Student("Alice", 20, 4.5),
    Student("Bob", 21, 3.8),
    Student("Charlie", 19, 4.2)
]

process_students(students)