# 3. TypedDict:
#   - Создайте файл "student_typeddict.py" для написания кода с использованием TypedDict.
#   - Импортируйте TypedDict из модуля typing.
#   - Определите TypedDict для представления данных о студентах.


from typing import TypedDict, List

class Student(TypedDict):
    name: str
    age: int
    average_score: float

def process_students(students: List[Student]):
    for student in students:
        print(f"Name: {student['name']}, Age: {student['age']}, Average Score: {student['average_score']}")

students = [
    Student(name="Alice", age=20, average_score=4.5),
    Student(name="Bob", age=21, average_score=3.8),
    Student(name="Charlie", age=19, average_score=4.2)
]

process_students(students)
