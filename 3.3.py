# magic methods __add__, __mul__, __sub__, __truediv__

class BankAccount:
    def __init__(self, name, balance):
        print('new obj init')
        self.name = name
        self.balance = balance

    def __repr__(self):
        return f"Client {self.name} balance {self.balance}"

    def __add__(self, other):
        print('__add__ called')
        if isinstance(other, (int, float)):
            return self.balance + other
        if isinstance(other, BankAccount):
            # return self.balance + other.balance
            return BankAccount(self.name, self.balance + other)
        raise NotImplemented

    def __radd__(self, other):
        print('__radd__ called')
        return self + other

    def __mul__(self, other):
        print('__add__ called')
        if isinstance(other, (int, float)):
            return self.balance * other
        if isinstance(other, BankAccount):
            return self.balance * other.balance
        if isinstance(other, str):
            return self.name + other
        raise NotImplemented


# b = BankAccount('ivan', 5000)
# d = BankAccount('masha', 7000)
# id(b)
# id(d)
# print(b + 600)
# print(b + d)
# print(d * 566)
# print(d * 566)
# id(b)
# id(d)


# ---

class Vector:
    def __init__(self, *args):
        self.values = sorted([i for i in args if isinstance(i, int)])

    def __str__(self):
        if len(self.values):
            return f'Вектор{tuple(self.values)}'
        return 'Пустой вектор'

    def __add__(self, other):

        if isinstance(other, int):
            return Vector(*[i + other for i in self.values])

        elif isinstance(other, Vector):
            if len(other) != len(self.values):
                return 'Сложение векторов разной длины недопустимо'
            return Vector(*[self.values[i] + other.values[i] for i, val in enumerate(self.values)])

        else:
            return print(f'Вектор нельзя сложить с {other}')

    def __len__(self):
        return len(self.values)

    def __mul__(self, other):
        if isinstance(other, int):
            return Vector(*[i * other for i in self.values])

        elif isinstance(other, Vector):
            if len(other) != len(self.values):
                return 'Умножение векторов разной длины недопустимо'
            return Vector(*[self.values[i] * other.values[i] for i, val in enumerate(self.values)])
        else:
            print(f'Вектор нельзя умножать с {other}')


v1 = Vector(1, 2, 3)
print(v1)  # печатает "Вектор(1, 2, 3)"

v2 = Vector(3, 4, 5)
print(v2)  # печатает "Вектор(3, 4, 5)"
v3 = v1 + v2
print(v3)  # печатает "Вектор(4, 6, 8)"
v4 = v3 + 5
print(v4)  # печатает "Вектор(9, 11, 13)"
v5 = v1 * 2
print(v5)  # печатает "Вектор(2, 4, 6)"
v5 + 'hi'  # печатает "Вектор нельзя сложить с hi"
v6 = v1 * v4
v6 * 'hi'
print(v6)
