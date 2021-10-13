class Notebook:

    def add(self, name, price):
        with open("note.txt", "a") as add_file:
            add_file.write(f"{name} - {price}$\n")
            print("\'Запись создана\'")

    def find(self, name):
        with open("note.txt") as find_file:
            for line in find_file:
                if name in line:
                    print(line)

    def info(self):
        with open("note.txt") as file:
            print(file.read())

    def delete(self, names):
         with open("note.txt", 'r+') as del_file:
            data = ''.join(filter(lambda l: names not in l, del_file))
            del_file.seek(0)
            del_file.truncate(0)
            del_file.write(data)
            return f"'{names}' удален"

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
        book.add(name, price)

    elif command == '2':
        name = input("Чтобы найти, введите название покупки: ")
        book.find(name)

    elif command == '3':
        book.info()

    elif command == '4':
        names = input("Введите покупку которую хотите удалить:  ")
        print(book.delete(names))

    elif command == '5':
        break

    else:
        print('Неизвестная команда')
