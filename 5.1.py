# Exceptions

print('hello')
print('hello')
print('hello')
print('hello')
print('hello')
try:
    '789'[5]
except IndexError:
    print('erorr scuko')
print('hello')
print('hello')
print('hello')
# raise ValueError('ffffuuuuuuuuuuuuuuu')  # self made exception
print('hello')

t = IndexError()


def get_mro(cls):
    print(*[c.__name__ for c in cls.mro()], sep=' -> ')


get_mro(IndexError)  # Exceptions MRO  line


class Wallet:
    def __init__(self, currency, balance):
        if not isinstance(currency, str):
            raise TypeError('Неверный тип валюты')
        if len(currency) != 3:
            raise NameError('Неверная длина названия валюты')
        if not currency.isupper():
            raise ValueError('Название должно состоять только из заглавных букв')
        self.currency = currency
        self.balance = balance

    def __eq__(self, other):
        if not isinstance(other, Wallet):
            raise TypeError(f'Wallet не поддерживает сравнение с {other}')
        if self.currency != other.currency:
            raise ValueError('Нельзя сравнить разные валюты')
        if self.balance == other.balance:
            return True
        return False

    def __add__(self, other):
        if not isinstance(other, Wallet) or self.currency != other.currency:
            raise ValueError('Данная операция запрещена')
        return Wallet(self.currency, self.balance + other.balance)

    def __sub__(self, other):
        if not isinstance(other, Wallet) or self.currency != other.currency:
            raise ValueError('Данная операция запрещена')
        return Wallet(self.currency, self.balance - other.balance)

wallet1 = Wallet('USD', 50)
wallet2 = Wallet('RUB', 100)
wallet3 = Wallet('RUB', 150)
# wallet4 = Wallet(12, 150)  # исключение TypeError('Неверный тип валюты')
# wallet5 = Wallet('qwerty', 150)  # исключение NameError('Неверная длина названия валюты')
# wallet6 = Wallet('abc', 150)  # исключение ValueError('Название должно состоять только из заглавных букв')
print(wallet2 == wallet3)  # False
# print(wallet2 == 100)  # TypeError('Wallet не поддерживает сравнение с 100')
# print(wallet2 == wallet1)  # ValueError('Нельзя сравнить разные валюты')
wallet7 = wallet2 + wallet3
print(wallet7.currency, wallet7.balance)  # печатает 'RUB 250'
# wallet2 + 45  # ValueError('Данная операция запрещена')
