def notebook():

    todo_list = []

    def add_todo(arg):

        todo_list.append(arg)

        return todo_list

    return add_todo

    # def get_all():
    #
    #
    #     print(todo_list)
    # return get_all()

notebook()
# my_day("дело №1")
# my_day("дело №2")
# print(my_day("qwert"))
