# Создать класс Rectangle:
# -конструктор принимает две стороны x,y
# -описать арифметические методы:
#   + сума площадей двух экземпляров класса
#   - разница площадей
#   == или площади равны
#   != не равны
#   >, < меньше или больше
#   при вызове метода len() подсчитывать сумму сторон

# class Rectangle:
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __add__(self, other):
#         return self.x + other.x, self.y + other.y
#
#     def __sub__(self, other):
#         return self.x - other.x, self.y - other.y
#
#     def __eq__(self, other):
#         return self.x == other.x, self.y == other.y
#
#     def __ne__(self, other):
#         return self.x != other.x, self.y != other.y
#
#     def __lt__(self, other):
#         return self.x < other.x, self.y < other.y
#
#     def __gt__(self, other):
#         return self.x > other.x, self.y > other.y
#
#     def __len__(self):
#         return self.x + self.y
#
# rectangle1 = Rectangle(3, 6)
# rectangle2 = Rectangle(4, 8)
#
# print(rectangle1 + rectangle2)
# print(rectangle1 - rectangle2)
# print(rectangle1 == rectangle2)
# print(rectangle1 != rectangle2)
# print(rectangle1 < rectangle2)
# print(rectangle1 > rectangle2)
# print(len(rectangle1))
# print(len(rectangle2))
#######################################################################################################################
# 1)Створити пустий list
# 2)Створити клас Letter
# 3) створити змінну класу __count.
# 4) при створенні об'єкта має створюватись змінна об'єкта(пропертя) __text, для цієї змінної мають бути гетер і сетер
# 5) при створені об'єкта, __count має збільшуватися на 1
# 6) має бути метод(метод класу) для виводу __сount
# 7) має бути метод який записує в наш ліст текст з нашої змінної __text

# list1 = []
# 
# class Letter:
# 
#     __count = 0
# 
#     def __init__(self, text):
#         self.__text = text
#         # self.__class__.__count += 1
#         Letter.__count += 1
#         self.id = Letter.__count
# 
#     @classmethod
#     def get_count(cls):
#         print(f"We have '{cls.__count}' objects.")
# 
#     def __getText(self):
#         return self.__text
# 
#     def __setText(self, new_value):
#         self.__text = new_value
#         list1.append(new_value)
# 
#     text = property(__getText, __setText)

# letter = Letter("")
# letter1 = Letter("")
# letter2 = Letter("")
# Letter.get_count()
# letter.text = "new text"
# letter1.text = "some text"
# letter2.text = "some new text"
# print(letter.text, letter1.text, letter2.text)
# print(list1)
#######################################################################################################################
# создать класс Human (name, age)
# создать два класса Prince и Cinderella:
# у золушки должно быть имя возраст и размер ноги
# у принца имя, возраст и размер найденой туфельки, так же должен быть метод который принимает лист золушек и ищет ту самую
#
# класса золушки должна быть переменная count которая будет считать сколько экземпляров класса золушка было создано
# и метод класса который будет показывать это количество

# class Human:
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# class Cinderella(Human):
#     __count = 0
#
#     def __init__(self, name, age, footSize):
#         super().__init__(name, age)
#         self.footSize = footSize
#         self.__class__.__count += 1
#
#     @classmethod
#     def get_count(cls):
#         return (f"We have << {cls.__count} >> objects of cinderallas")
#
#     def __str__(self):
#         return str(self.__dict__)
#
#     def __repr__(self):
#         return self.__str__()
#
# class Prince(Human):
#
#     def __init__(self, name, age, shoes):
#         super().__init__(name, age)
#         self.shoes = shoes
#
#     def find(self, cinderellas):
#         for cinderella in cinderellas:
#             if cinderella.footSize == prince.shoes:
#                 return (f"Our Cinderella is '{cinderella.name}'")
#
#
# cinderellas = [Cinderella("Anna", 18, 35),
#                Cinderella("Maria", 19, 36),
#                Cinderella("Katy", 20, 37)]
# prince = Prince("John", 22, 37)
#
# print(Cinderella.get_count())
# print(prince.find(cinderellas))
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
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

    def sum_price(self):
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
