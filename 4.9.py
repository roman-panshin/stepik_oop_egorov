# slots + property + inheritance


class Rectangle:
    __slots__ = ('__width', 'height')

    def __init__(self, a, b):
        self.width = a
        self.height = b

    @property
    def perimetr(self):
        return (self.height + self.width) * 2

    @property
    def area(self):
        return self.height * self.width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        print('setter')
        self.__width = value


class Square(Rectangle):
    pass


a = Rectangle(10, 20)
a.width = 100

print(a.perimetr)

s = Square(10, 8)

print(s.__dict__)
