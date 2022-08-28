# Property decorator


class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    @property
    def my_balance(self):  # getter with decorator
        print('getter')
        return self.__balance

    # my_property_balance = my_balance  # сохраняем свойство в переменную чтобы не затерлось следующей одноименной функцией

    @my_balance.setter
    def my_balance(self, value):  # setter with decorator
        print('setter')
        if not isinstance(value, (int, float)):
            raise ValueError('balance must be a numeric')
        self.__balance = value

    # my_balance = my_property_balance.setter(my_balance)

    @my_balance.deleter
    def my_balance(self):  # deleter with decorator
        print('delete')
        del self.__balance

    # my_balance = my_balance.getter(get_balance)
    # my_balance = my_balance.setter(set_balance)
    # my_balance = my_balance.deleter(delete_balance)

    # balance = property(fget=get_balance,
    #                    fset=set_balance,
    #                    fdel=delete_balance)  # property


#
# b = BankAccount('ivan', 1000)
# print(b.my_balance)
#
# b.my_balance = 500
# print(b.my_balance)
#
# del b.my_balance
# print(b.my_balance)


# ---

class Notebook:
    def __init__(self, notes):
        self._notes = notes

    @property
    def notes_list(self):
        index = 1
        for value in self._notes:
            print(f'{index}.{value}')
            index += 1
        return


# note = Notebook(['Buy Potato', 'Buy Carrot', 'Wash car'])
# note.notes_list


# ---

class Square:
    def __init__(self, side):
        self.side = side

    @property
    def side(self):
        print('get side')
        return self._side

    @side.setter
    def side(self, value):
        print('set side')
        self._side = float(value)

    @property
    def area(self):
        return self.side ** 2

    @area.setter
    def area(self, value):
        self.side = value ** 0.5


# sq = Square(428)
#
# print(sq.side)
#
# print(sq.area)
#
# sq.area = 100
#
# print(sq.side)


# ---

