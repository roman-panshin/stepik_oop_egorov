# Property decorator
import hashlib
import os


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

class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password

    @property
    def password(self):
        raise AttributeError('password only change, not show')

    @password.setter
    def password(self, plaintext):
        salt = os.urandom(32)
        self._hashed_password = hashlib.pbkdf2_hmac(
            "sha256", plaintext.encode("utf-8"), salt, 100_000
        )


#
# jack = User("Jack", "secret_key")
# print(jack._hashed_password)
# jack.password = "new_secret"
# print(jack._hashed_password)

# ---

class Money:
    def __init__(self, dollars, cents):
        self.total_cents = cents + dollars * 100

    @property
    def dollars(self):
        return self.total_cents // 100

    @dollars.setter
    def dollars(self, value):
        if not isinstance(value, int) or value < 0:
            print('Error dollars')
        else:
            self.total_cents = value * 100 + self.total_cents % 100

    @property
    def cents(self):
        return self.total_cents % 100

    @cents.setter
    def cents(self, value):
        if not isinstance(value, int) or value < 0 or value >= 100:
            print('Error cents')
        else:
            self.total_cents = value + (self.total_cents // 100) * 100

    def __str__(self):
        return f"Ваше состояние составляет {self.dollars} долларов {self.cents} центов"


# bablo = Money(100, 25)
#
# print(bablo.dollars)
# print(bablo.total_cents)
#
# bablo.dollars = 77
# bablo.cents = 34
#
#
# print(bablo.dollars)
# print(bablo.total_cents)


Bill = Money(101, 99)
print(Bill)  # Ваше состояние составляет 101 долларов 99 центов
print(Bill.dollars, Bill.cents)  # 101 99
print(Bill.total_cents)  # 10199
Bill.dollars = 123
print(Bill)  # Ваше состояние составляет 666 долларов 99 центов
Bill.cents = 100
print(Bill)  # Ваше состояние составляет 666 долларов 12 центов
