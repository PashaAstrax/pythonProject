# 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
# наприклад:
# st = 'as 23 fdfdg544' введена строка
# 2,3,5,4,4        #вивело в консолі.

# st = 'as 23 fdfdg544'
# r = st.replace(" ", "")
# print(', '.join(i for i in r if i.isdigit()))
#################################################################################
# 2)написати прогу яка вибирає зі введеної строки числа і виводить їх
# так як вони написані
# наприклад:
#   st = 'as 23 fdfdg544 34' #введена строка
#   23, 544, 34              #вивело в консолі

# st = 'as 23 fdfdg544 34'
# for i in st:
#     if not i.isalpha():
#         print(i, end="")
#################################################################################
# list comprehension
#
# 1)есть строка:
# greeting = 'Hello, world'
# записать каждый символ в лист поменяв его на верхний регистр
# пример:
# ['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']

# print(list((",").join(greeting.upper().split(","))))


# 2) с диапазона от 0-50 записать в лист только не парные числа, при этом возвести их в квадрат
# пример:
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]

# print(list(i**2 for i in range(1, 50, 2)))
#################################################################################
# function
#
# - створити функцію яка виводить ліст
# def list_1():
#     return list()
# print(list_1())

# - створити функцію яка приймає три числа та виводить та повертає найменьше.
# def min_num(a, b, c):
#     return min(a, b ,c)
# print(min_num(8, 7, 44))

# - створити функцію яка приймає три числа та виводить та повертає найбільше.
# def max_num(a, b, c):
#     return max(a, b, c)
# print(max_num(4, 43, 76))

# - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше
# def m(*args):
#     return min(args)
# print(m(max(3, 6, 8, 9)))

# - створити функцію яка повертає найбільше число з ліста
# def max_list(arr):
#     return max(arr)
# print(max_list([1, 4, 88, 55]))

# - створити функцію яка повертає найменьше число з ліста
# def min_list(arr):
#     return min(arr)
# print(min_list([1, 4, 88, 55]))

# - створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.
# def list_num(arr):
#     return sum(arr)
# print(list_num([4, 8, 33, 11]))

# - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.
# def middle_num(arr):
#     return int(sum(arr)/len(arr))
# print(middle_num([4, 3, 7, 44, 2]))
#################################################################################
# decorators
# - є функція:
# def pr():
#     return 'Hello_boss_!!!'
#  написати декоратор до цієї функції, який замінює нижні підчеркування на пробіли і повертає це значення

# def decor(func):
#     def inner():
#         func(a="_", b=" ")
#     return inner
#
# @decor
# def pr(a, b):
#     print("Hello_boss_!!!".replace(a, b))
# pr()