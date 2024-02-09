# n = int(input('введите число n: '))
# i = 2
# fac = 2
# while i <= n:
#     fac = fac * i
#     i += 1
# print(fac)

# A = int(input('Ввведите число А: '))
# number = 3
# f1 = 1
# f2 = 1
# while f2 < A:
#     f1, f2 = f2, f1+f2
#     number += 1
# if f2 == A:
#     print(number)
# else:
#     print(-1)

#
# import random
# d = int(input('Введите число дней для провер: '))
# max = 0
# count = 0
# for _ in range(d):
#     temp = random.randint(-50, 50)
#     print(temp)
#     if temp > 0:
#        count += 1
#        if max < count:
#            max = count
#     else:
#        count = 0
#
# print(f'{max} число макс повторений')

# import random  # Импортировать в начале
#
# n = int(input('введите число N: '))
# min_ = float('inf')
# max_ = float('-inf')
#
# for i in range(1, n):
#     mass = random.randint(1, 51)
#
#     print(mass)
#     if mass > max_:
#         max_ = mass
#     if mass < min_:
#         min_ = mass
#
# print(f"max= {max_}, min = {min_}")

