"""Напишите функцию, которая принимает два числа и возвращает результат
суммы целых чисел в этом диапазоне"""
def sum_numbers(num_1, num_2):
    if num_1 < num_2:
        return sum(range(num_1, num_2+1))
    else:
        return sum(range(num_1, num_2+1))
print(sum_numbers(1, 10))







