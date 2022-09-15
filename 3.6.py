# magic method __bool__

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self):
        return abs(self.x - self.y)

    def __bool__(self):
        return self.x != 0 or self.y != 0


#
# p1 = Point(1, 2)
# p2 = Point(0, 0)
# p3 = Point(1, 2)
#
# if p2:
#     print('true')
#
# print(bool(p1))
# print(bool(p2))

class City:
    def __init__(self, name):
        self.name = str(name).title()

    def __str__(self):
        return self.name

    def __bool__(self):
        return self.name[-1] not in ['a', 'e', 'i', 'o', 'u']


# p1 = City('new york')
# print(p1)  # печатает "New York"
# print(bool(p1))  # печатает "True"
# p2 = City('SaN frANCISco')
# print(p2)  # печатает "San Francisco"
# print(p2 == True)  # печатает "False"


class Quadrilateral:
    def __init__(self, *args):
        self.width = self.height = args[0]
        if len(args) > 1:
            self.height = args[1]

    def __str__(self):
        if self.__bool__():
            return f'Куб размером {self.width}х{self.height}'
        return f'Прямоугольник размером {self.width}х{self.height}'

    def __bool__(self):
        if self.width == self.height:
            return True
        return False


q1 = Quadrilateral(10)
print(q1)  # печатает "Куб размером 10х10"
print(bool(q1))  # печатает "True"
q2 = Quadrilateral(3, 5)
print(q2)  # печатает "Прямоугольник размером 3х5"
print(q2 == True)  # печатает "False"
