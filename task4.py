# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# m = "a a a b c a a d c d d"
# count = dict()
# massive = m.split()
# print(massive)
# for chr in massive:
#     key = chr
#     if chr in count:
#         count[key] += 1
#     else:
#         count[key] = 1
#
#
#
# print(count)
#
#
# string_ = "a a a b c a a d c d d"
# orig = string_.split()
# print(orig)
#
# newlist = []
# count_times = {}
#
# for symbol in orig:
#     if not symbol in count_times:
#         newlist.append(symbol)
#         count_times[symbol] = 1
#
#     else:
#         newlist.append(f'{symbol}_{count_times[symbol]}')
#         count_times[symbol] += 1
#
# print(" ".join(newlist))
# print(count_times)
#
# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells

# m = "She sells sea shells on the sea shore;The shells that she sells are sea shells I'm sure. So if she sells sea shells on the sea shore, I'm sure that the shells are sea shore shells."
# array = m.split()
# print(array)
# print(len(set(array)))
# print(set(array))

max_number = float("-inf")

while True:
    n = int(input())
    if n == 0:
        break
    if max_number < n:
        max_number = n

print(max_number)