# magic methods ___str__ and __repr__
import random


class Lion:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'the object Lion - {self.name}'

    def __str__(self):
        return f'Lion - {self.name} {"zloy" if random.randint(0, 1) == 0 else "dobriy"}'


#
# q = Lion('Bob')
# s = Lion('simba')
#
# print(str(q))
# print(str(s))

# ---

class Person:
    def __init__(self, name, surname, gender="male"):
        if gender not in ['male', 'female']:
            print("Не знаю, что вы имели ввиду? Пусть это будет мальчик!")
            gender = "male"
        self.gender = gender
        self.name = name
        self.surname = surname

    def __str__(self):
        if self.gender == 'male':
            return f'Гражданин {self.surname} {self.name}'
        return f'Гражданка {self.surname} {self.name}'


# p1 = Person('Chuck', 'Norris')
# print(p1) # печатает "Гражданин Norris Chuck"
# p2 = Person('Mila', 'Kunis', 'female')
# print(p2) # печатает "Гражданка Kunis Mila"
# p3 = Person('Оби-Ван', 'Кеноби', True)# печатает "Не знаю, что вы имели ввиду? Пусть это будет мальчик!"
# print(p3) # печатает "Гражданин Кеноби Оби-Ван"


# ---

class Vector:

    def __init__(self, *args):
        self.values = []
        for i in args:
            if isinstance(i, int):
                self.values.append(i)

    def __str__(self):
        if len(self.values):
            return f'Вектор({", ".join(map(str, sorted(self.values)))})'
        return 'Пустой вектор'


# v1 = Vector(1, 2, 0)
# print(v1)  # печатает "Вектор(1, 2, 3)"
# v2 = Vector()
# print(v2)  # печатает "Пустой вектор"


# ---

class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"__str__ method: {self.first_name} {self.last_name}"

    def __repr__(self):
        return f"__repr__ method: {self.first_name} {self.last_name}"


user = User("Vasya", "Pypkin")
print(f"{repr(user)}")

# или лучше воспользоваться !r
print(f"{user!r}")
