class Notebook:

    def __init__(self):
        self.jotter = {}

    def add(self, key, val):
        self.jotter[key] = val
        return "\'Запись создана\'"

    def find(self, name):
        if name in self.jotter:
            data = ' '.join(self.jotter[name])
            return f"name: '{name.capitalize()}', price: {data}$"
        return "\'Покупка не найдена\'"

    def info(self):
        return self.jotter.items()

    def delete(self, name):
        if name in self.jotter:
            del self.jotter[name]
            return f'"{name}" удален'
        return "\'Нет такого в списке\'"

print('''\nВыберите что вы хотите сделать:
    * 1 - Создать запись
    * 2 - Поиск по названию покупки
    * 3 - Список все записей
    * 4 - Удалить запись
    * 5 - выход''')

book = Notebook()
while True:

    command = input("\nВведите команду: ")

    if command == '1':
        name = input("Введите название покупки: ")
        price = input("Введите цену покупки: ")
        print(book.add(name, [price]))

    elif command == '2':
        name = input("Чтобы найти, введите название покупки: ")
        print(book.find(name))

    elif command == '3':
        for name, data in book.info():
            data = ' '.join(data)
            print(f"name: '{name.capitalize()}', price: {data}$")

    elif command == '4':
        name = input("Введите покупку которую хотите удалить:  ")
        print(book.delete(name))

    elif command == '5':
        break

    else:
        print('Неизвестная команда')
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
