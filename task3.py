# data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# k = -2
#
# if k > 0:
#     for i in range(k):
#         data.insert(0, data.pop(-1))
# else:
#     for i in range(k * -1):
#         print(i)
#         data.append(data.pop(0))
#
# print(data)
#
#
# data = [1, 2, 3, 4, 5, 6, 7]
# k = 3
# new_data = data[len(data)-k:] + data[:len(data)-k]
# print(new_data)
#
# Задача №21. Решение в группах
# Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
# Примечание: Список словарей задан изначально.
# Пользователь его не вводит
L = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
print("Original List: ",L)
s = set()
for dic in L:
   for val in dic.values():
      s.add(val)
print(s)