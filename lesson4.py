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
#         self.__class__.__count += 1
#
#     @classmethod
#     def get_count(cls):
#         return (f"We have '{cls.__count}' objects.")
#
#     def __getText(self):
#         return self.__text
#
#     def __setText(self, new_value):
#         self.__text = new_value
#         list1.append(new_value)
#
#     text = property(__getText, __setText)
#
# letter = Letter("")
# letter1 = Letter("")
# letter2 = Letter("")
# print(Letter.get_count())
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

class Human:

    def __init__(self, name, age):
        self.name = name
        self.age = age

class Cinderella(Human):

    __count = 0

    def __init__(self, name, age, footSize):
        super().__init__(name, age)
        self.footSize = footSize
        self.__class__.__count += 1

    @classmethod
    def get_count(cls):
        return cls.__count

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return self.__str__()


class Prince(Human):

    def __init__(self, name, age, shoes):
        super().__init__(name, age)
        self.shoes = shoes

    # def find(self):



cinderellas = [Cinderella("Anna", 18, 35), Cinderella("Ira", 19, 36), Cinderella("Olga", 20, 37)]

prince = Prince("John", 22, 37)

# print(cinderellas)
# print(Cinderella.get_count())

