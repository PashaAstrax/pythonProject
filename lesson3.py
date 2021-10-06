# def notebook():
#
#     todo_list = []
#
#     def add_todo(*args: str) -> list:
#
#         todo_list.append(*args)
#
#         return todo_list
#
#     return add_todo
#
#     def get_all():
#
#         # print(todo_list)
#
#         return get_all
#
# my_day = notebook()
# print(my_day("qwert"))
# print(my_day("asdf"))
#####################################################################################
# 3) С помощью lambda функции извлеките из списка числа, делимые на 15 без остатка.

# list1 = [76, 60, 45, 89, 100, 105]

# print(list(filter(lambda x: x % 15 == 0, list1)))
#####################################################################################
# 4) написать функцию которая будет принимать целое число n и посчитайте n + nn + nnn.
# Пример:
# summ(7) -> 7+77+777=861

# def func(n):
#     n1 = n
#     n2 = int(str(n) * 2)
#     n3 = int(str(n) * 3)
#     print(n1 + n2 + n3)
# func(7)