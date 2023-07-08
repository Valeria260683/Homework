"""Четность чисел"""
number_1 = 10
if number_1 % 2 == 0:
    print('Четное число')
else:
    print('Нечетное число')
number_2 = 17
if number_2 % 2 == 0:
    print('Четное число')
else:
    print('Нечетное число')

"""Поменять местами значения двух переменных"""
x = 5
y = 7
x, y = y, x
print(x)
print(y)
"""Из последовательности чисел составить список и кортеж """
nums = input("Ввести последовательность чисел : ")
nums_1 = nums.split(" ")
nums_2 = tuple(nums_1)
print(nums_1)
print(nums_2)
