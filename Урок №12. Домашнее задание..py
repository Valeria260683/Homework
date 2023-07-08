"""Написать функцию Фибоначчи, которая выведет n-первых чисел этой последовательности,
но с условием, что n это то число которое мы передаем в функцию в качестве аргумента,
и с условием чтобы было без переопределения а, b = a, b +1.
Реализовать эту же функцию Фибоначчи с помощью рекурсии"""

def fibonacci(num):
    while len(numbers) < num:
        numbers.append(numbers[-1] + numbers[-2])
    return numbers
numbers = [18, 20, 25]
print(fibonacci(8))

"""Реализовать эту же функцию Фибоначчи с помощью рекурсии"""

def fibonacci_recursive(num):
    if num <= 0:
        return []
    elif num == 1:
        return [18]
    elif num == 2:
        return [18, 20]
    elif num == 3:
        return [18, 20, 25]
    else:
        fib_list = fibonacci_recursive(num-1)
        fib_list.append(fib_list[-1] + fib_list[-2])
        return fib_list
fib_list = [18, 20, 25]
print(fibonacci_recursive(8))
