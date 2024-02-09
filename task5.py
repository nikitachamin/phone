# def fibonacci(n):
#     if n in (1, 2):
#         return 1
#     return fibonacci(n - 1) + fibonacci(n - 2)
#
#
# print(fibonacci(7))

#
# list_ = [1, 3, 3, 3, 4]
# output = []
# my_max = max(list_)
# my_min = min(list_)
# for elem in list_:
#     if elem == my_max:
#         output.append(my_min)
#     else:
#         output.append(elem)
#
# print(*output)

# def numbers(n):
#     result = "Да"
#     for i in range(2, n):
#         if n % i == 0 :
#             result = "Нет"
#             break
#     print(result)
#
# numbers(14)

# n = int(input("Введите количество число: "))
#
# def funs(n):
#     if n == 0:
#         return " "
#     num = input("Введите число: ")
#     return f"{funs(n - 1)} {num}"
#
# print(funs(n))