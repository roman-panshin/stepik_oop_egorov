# computed property

class Square:
    def __init__(self, s):
        self.__side = s
        self.__area = None

    @property
    def side(self):
        return self.__side

    @side.setter
    def side(self, value):
        self.__side = value
        self.__area = None  # reset area for next calculation

    @property
    def area(self):
        if self.__area is None:
            print('calculate area')
            self.__area = self.side ** 2
        return self.__area


# b = Square(100)
# print(b.area)
# print(b.area)
# print(b.area)
#
# print(b.area)
# b.side = 8
# print(b.area)
# print(b.area)


# ---

class Rectangle:
    def __init__(self, l, h):
        self.length = l
        self.height = h

    @property
    def area(self):
        return self.length * self.height


# r1 = Rectangle(3, 5)
# r2 = Rectangle(6, 1)
#
# print(r1.area) # 15
# print(r2.area) # 6


# ---

one_dollar = 112
print(f"{one_dollar:04}")  # выводит число с указанным кол-вом нулей перед ним


class Date:
    def __init__(self, d, m, y):
        self.day = d
        self.month = m
        self.year = y

    @property
    def date(self):
        return f'{self.day:02}/{self.month:02}/{self.year:04}'

    @property
    def usa_date(self):
        return f'{self.month:02}-{self.day:02}-{self.year:04}'


d1 = Date(5, 10, 2001)
d2 = Date(15, 3, 999)

print(d1.date) # 05/10/2001
print(d1.usa_date) # 10-05-2001
print(d2.date) # 15/03/0999
print(d2.usa_date) # 03-15-0999
