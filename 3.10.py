# magic methods __iter__, ___next__
class Mark:
    def __init__(self, values):
        self.value = values
        self.index = 0

    def __next__(self):
        if self.index >= len(self.value):
            self.index = 0
            raise StopIteration
        letter = self.value[self.index]
        self.index += 1
        return letter

    def __iter__(self):
        return self


class Student:
    def __init__(self, name, surname, marks):
        self.surname = surname
        self.name = name
        self.marks = marks

    def __getitem__(self, item):
        return self.marks[item]

    def __iter__(self):
        print('call iter')
        self.index = 0
        return iter(self.marks)

    def __next__(self):
        if self.index >= len(self.name):
            raise StopIteration
        letter = self.name[self.index]
        self.index += 1
        return letter


# m = Mark([2, 3, 4, 5, 4, 3, 2, 2, 3, 4, 4, 5, 3, 4])
#
# igor = Student('ivaniva', 'ivanov', m)
# for i in igor:
#     print(i)

class PowerTwo:
    def __init__(self, num):
        self.num = num

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index > self.num:
            raise StopIteration
        res = 2 ** self.index
        self.index += 1
        return res


# numbers = PowerTwo(2)
#
# iterator = iter(numbers)
#
# print(next(iterator))  # печатает 1
# print(next(iterator))  # печатает 2
# print(next(iterator))  # печатает 4
# print(next(iterator))  # исключение StopIteration

class InfinityIterator:

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        res = 10 * self.index
        self.index += 1
        return res


a = iter(InfinityIterator())
print(next(a))
print(next(a))
print(next(a))
print(next(a))
