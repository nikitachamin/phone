# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.
# def print_operation_table(operation, num_rows = 9, num_columns = 9):
#     if num_rows < 3 or num_columns < 3:
#         print("ОШИБКА! Размерности таблицы должны быть больше 2!")
#         return False
#     for i in range(1, num_rows+1):
#         answer = []
#         for j in range(1, num_columns+1):
#             answer.append(str(operation(i,j)))
#         print(' '.join(f'{i}' for i in answer))
#
#
# print_operation_table(lambda x, y: x * y, 4, 4)

stroka = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
def rytm(stroka):
    phase = stroka.split()
    count_vowels = []
    if " " not in stroka:
        print("Количество фраз должно быть больше одной!")
        return False
    for word in phase:
        vowels = 0
        for i in word:
            if i in 'аеёиоуыэюя':
                vowels += 1
        count_vowels.append(vowels)
    if len(set(count_vowels)) == 1:
        print('Парам пам-пам')
    else:
        print("Пам парам")
rytm(stroka)
