#
# def f(a,b, result = 1):
#     if b == 0:
#         return result
#     else:
#         return a * f(a, b - 1)
#
#
# a = 3
# b = 5
# print(f(a, b))

# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
#
# Функция не должна ничего выводить, только возвращать значение.

#
# def sum_(a,b):
#     if b == 0:
#         return a
#     else:
#         return sum_(a+1, b -1)
#
# a = 3
# b = 5
# print(sum_(a, b))