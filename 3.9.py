#  magic methods __getitem__, __setitem__, __delitem__

class Vector:

    def __init__(self, *args):
        self.values = list(args)

    def __repr__(self):
        return str(self.values)

    def __getitem__(self, item):
        if 1 <= item <= len(self.values):
            return self.values[item - 1]  # change index interval
        else:
            raise IndexError('index error')

    def __setitem__(self, key, value):
        if 0 <= key <= len(self.values):
            self.values[key] = value
        elif key > len(self.values):  # if key more than len
            diff = key - len(self.values)
            self.values.extend([0] * diff)  # fill spaces with nuls
            self.values[key - 1] = value

        else:
            raise IndexError('index error')

    def __delitem__(self, key):
        if 0 <= key < len(self.values):
            del self.values[key]
        else:
            raise IndexError('index error')


# v3 = Vector(0, 10, 20, 2330, 312320, 23, 23)
#
# v3[150] = 100
#
# del v3[1]
#
# print(v3)


class Building:

    def __init__(self, stages):
        self.stages = []
        self.stages.extend(['None'] * stages)

    def __setitem__(self, key, value):
        if 0 <= key <= len(self.stages):
            self.stages[key] = value
        else:
            raise IndexError('index error')

    def __getitem__(self, key):
        if 0 <= key <= len(self.stages):
            return self.stages[key]
        else:
            raise IndexError('index error')

    def __delitem__(self, key):
        if 0 <= key <= len(self.stages):
            self.stages[key] = 'None'
        else:
            raise IndexError('index error')


iron_building = Building(22)  # Создаем здание с 22 этажами
iron_building[0] = 'Reception'
iron_building[1] = 'Oscorp Industries'
iron_building[2] = 'Stark Industries'
print(iron_building[2])
del iron_building[2]
print(iron_building[2])

print([None] * 10)
