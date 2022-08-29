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

