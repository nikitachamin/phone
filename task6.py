# import random
#
# n = 10
# m = 10
# list_first = [random.randint(1, 10) for _ in range(n)]
# list_second = [random.randint(1, 10) for _ in range(m)]
# print(list_first, list_second)
# output = []
# for i in list_first:
#     for j in list_second:
#         if i == j:
#            break
#     else:
#        output.append(i)
#
#
# print(output)
#
# def array_diff(a, b):
#     return [x for x in a if x not in b]
#
# print(array_diff(list_first, list_second))
#
# import random
# n = int(input())
# list_first = [random.randint(1, 10) for _ in range(n)]
# print(list_first)
# temp = 0
# for i in range(1,len(list_first)-1):
#     if list_first[i-1] < list_first[i] > list_first[i+1]:
#         temp += 1
# print(temp)

#
# import random
# n = int(input())
# list = [random.randint(1, 10) for _ in range(n)]
# print(list)
# count = 0
# for i in range(len(list)):
#     for j in range(i,len(list)):
#         if i != j and list[i] == list[j]:
#            count += 1
# print(count)

# def sum_del(num):
#     count = 1  # Суммма делителей, начинаем считать со 2 -го
#     for i in range(2, int(num ** 0.5) + 1):  # 1 2 4 5 10 20 25 50
#         if num % i == 0:
#             # print (i, num //2)
#             count += i
#             if i != num // i:
#                 count += num // i
#     return (count)
#
#
# # print(sum_del(220))
# # print(sum_del(sum_del(220)))
#
# for n in range(1, 100_000):
#     m = sum_del(n)
#     if n < m and (n == sum_del(m)):
#         print(n, m)