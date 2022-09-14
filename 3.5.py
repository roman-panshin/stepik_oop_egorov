# magic methods __eq__, __hash__

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):  # hash was crashed
        return isinstance(other, Point) and \
               self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))


# p1 = Point(1, 2)
#
# p2 = Point(3, 4)
#
# print(p1 == p2)
#
# print(hash(p1))
# print(hash(p2))
#
# r = {}
# r[p1] = 100
#
# print(r)


'''
Чтобы не реализовывать все магические методы сравнения, 
можно использовать декоратор functools.total_ordering, 
который позволяет  сократить код, реализовав только методы __eq__ и __lt__
'''
from functools import total_ordering


@total_ordering
class Account:
    def __init__(self, balance):
        self.balance = balance

    def __eq__(self, other):
        return self.balance == other.balance

    def __lt__(self, other):
        return self.balance < other.balance


acc1 = Account(10)
acc2 = Account(20)
print(acc1 > acc2)
print(acc1 < acc2)
print(acc1 == acc2)
print(acc1 != acc2)
print(acc1 >= acc2)
print(acc1 <= acc2)


'''
Хотя этот декоратор позволяет создавать хорошо управляемые 
и полностью упорядоченные типы, это происходит за счет более 
медленного выполнения и более сложных трассировок стека для 
производных методов сравнения. Если анализ производительности 
показывает, что это является узким местом для данного приложения, 
реализация всех шести методов сравнения обеспечит повышение скорости
'''
