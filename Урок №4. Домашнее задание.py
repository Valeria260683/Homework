"""Посчитать сумму четных чисел от 0 до 100 с помощью цикла for"""
numbers = 0
for i in range(100):
 if i % 2 == 0:
    numbers += i
print(numbers)



