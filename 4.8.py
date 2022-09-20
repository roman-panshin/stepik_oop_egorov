#  Slots

from timeit import timeit


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


class PointSlots:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


s = Point(3, 4)
print(s.__sizeof__(), s.__dict__.__sizeof__())

s1 = PointSlots(3, 4)
print(s1.__sizeof__())  # slots has no __dict__ and take less place

s1.q = 100  # error - only attributes from slots list


def make_c11():
    s = Point(3, 4)
    s.x = 100
    s.x
    del s.x


def make_c12():
    s = PointSlots(3, 4)
    s.x = 100
    s.x
    del s.x


print(timeit(make_c11))
print(timeit(make_c12))  # faster than without slots
