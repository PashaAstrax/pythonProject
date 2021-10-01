# 1)Дан лист:
list = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
#   - найти min число в листе
#   - удалить все дубликаты в листе
#   - заменить каждое четвертое значение на "Х"

# def min_number(num):
#     x = num[0]
#     for i in num:
#         if i < x:
#             x = i
#     return x
# print("min_num: " + str(min_number(list)))

# list1 = []
# for i in list:
#     if i not in list1:
#         list1.append(i)
#         list = list1
# print(list)

# arr = []
# index = 0
# for i in list:
#     arr.append(index)
#     index += 1
#     if index % 4 == 0:
#         i = "x"
#     print(i, end=", ")



# 2)вывести на экран пустой квадрат из "*" сторона которого указана в переменой:

# num = int(input("Введите число: "))
# print("* " * num)
# for i in range(num - 2):
#     print("* ", "  " * (num - 3), "* ")
# print("* " * num)


# 3) вывести табличку умножения с помощью цикла while

# x = 1
# while x < 10:
#     print(x, end="")
#     y = 2
#     while y < 10:
#          print('{:4n}'.format(x * y), end="")
#          y += 1
#     x += 1
#     print()


# 4) переделать первое задание под меню с помощью цикла

# def menu():
#     choice = input("\n==========================\n"
#             "1. Найти min число в листе;\n"
#             "2. Удалить все дубликаты в листе;\n"
#             "3. Заменить каждое четвертое значение на Х;\n"
#             "4. Вывести элемент листа, значение которого ближе всего к среднему арифметическому всех чисел;\n"
#             "5. Выход.\n"
#             "==========================\n"
#             "Сделайте свой выбор: ")
#     return int(choice)
#
# while True:
#     choice = menu()
#     if choice == 1:
#         print(list, "\nmin_num: " + str(min(list)))
#
#     elif choice == 2:
#         print(set(list))
#
#     elif choice == 3:
#         arr = []
#         index = 0
#         for i in list:
#             arr.append(index)
#             index += 1
#             if index % 4 == 0:
#                 i = "x"
#             print(i, end=" ")
#
#     elif choice == 4:
#         def middle_num(list):
#             a = list[::]
#             x = sum(list) / len(list)
#             for i, v in enumerate(list):
#                 list[i] = abs(v - x)
#             v = min(list)
#             return a[list.index(v)]
#         print(list)
#         print(middle_num(list))
#
#     elif choice == 5:
#         break


# ***  - вывести элемент листа, значение которого ближе всего к среднему арифметическому всех элементов этого же листа
# пример:
# [1, 2, 3, 4, 5, 6, 7, 8, 9] => 5
# [-1, -2, 3, 4, 555] => 4
# [5, 5, 5, 5] => 5
# [-10, 5, 5] => 5

# def middle_num(list):
#     a = list[::]
#     x = sum(list) / len(list)
#     for i, v in enumerate(list):
#         list[i] = abs(v - x)
#     v = min(list)
#     return a[list.index(v)]
#
# print(middle_num(list))