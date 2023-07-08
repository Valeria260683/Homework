"""Написать функцию, кoторая принимает два числа в качестве аргумента и посчитает наименьшее общее кратное
 для этих чисел"""
def gcd(num_1, num_2):
    if num_2 == 0:
        return num_1
    else:
        return gcd(num_2, num_1 % num_2)
print(gcd(12, 18))

def lcm(num_1, num_2):
    return num_1 * num_2 // gcd(num_1, num_2)
print(lcm(12, 18))