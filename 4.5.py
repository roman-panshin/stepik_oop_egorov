# delegating -call parent class from child class

# class Person:
#
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     def breathe(self):
#         print('Person breathe')
#
#
# class Doctor(Person):
#
#     def __init__(self, name, surname, age):
#         super().__init__(name, surname)  # call first
#         age.surname = age
#
#     def breathe(self):
#         print('Doctor breathe')
#         super().breathe()  # call to parent class


# p = Person()
# d = Doctor()
#
# d.breathe()


class Person:
    def __init__(self, name, passport):
        self.name = name
        self.passport = passport

    def display(self):
        print(f"{self.name}: {self.passport}")


class Employee(Person):
    def __init__(self, name, passport, salary, department):
        super().__init__(name, passport)
        self.salary = salary
        self.department = department


# a = Employee('Raul', 886012, 200000, "QA")
#
# a.display()  # печатает "Raul: 886012"

class Vehicle:

    def __init__(self, name, mileage, capacity):
        self.capacity = capacity
        self.mileage = mileage
        self.name = name

    def fare(self):
        return self.capacity * 100

    def display(self):
        print(f"Total {self.name} fare is: {self.fare()}")


class Bus(Vehicle):

    def __init__(self, name, mileage):
        super().__init__(name, mileage, 50)

    def fare(self):
        return super().fare() * 1.1


class Taxi(Vehicle):

    def __init__(self, name, mileage):
        super().__init__(name, mileage, 4)

    def fare(self):
        return super().fare() * 1.35


# sc = Vehicle('Scooter', 100, 2)
# sc.display()
#
# merc = Bus("Mercedes", 120000)
# merc.display()
#
# polo = Taxi("Volkswagen Polo", 15000)
# polo.display()


class Transport:
    def __init__(self, brand, max_speed, kind=None):
        self.brand = brand
        self.max_speed = max_speed
        self.kind = kind

    def __str__(self):
        return f"Тип транспорта {self.kind} марки {self.brand} может развить скорость {self.max_speed} км/ч"


class Car(Transport):
    def __init__(self, brand, max_speed, mileage, gasoline_residue):
        super().__init__(brand, max_speed, kind='Car')
        self.__gasoline_residue = gasoline_residue
        self.mileage = mileage

    @property
    def gasoline(self):
        return F"Осталось бензина на {self.__gasoline_residue} км"

    @gasoline.setter
    def gasoline(self, value):
        if isinstance(value, int):
            self.__gasoline_residue += value
            print(f"Объем топлива увеличен на {value} л и составляет {self.__gasoline_residue} л")
        else:
            print('Ошибка заправки автомобиля')


class Boat(Transport):
    def __init__(self, brand, max_speed, owners_name):
        super().__init__(brand, max_speed, kind='Boat')
        self.owners_name = owners_name

    def __str__(self):
        return f"Этой лодкой марки {self.brand} владеет {self.owners_name}"


class Plane(Transport):
    def __init__(self, brand, max_speed, capacity):
        super().__init__(brand, max_speed, kind='Plane')
        self.capacity = capacity

    def __str__(self):
        return f"Самолет марки {self.brand} вмещает в себя {self.capacity} людей"


# transport = Transport('Telega', 10)
# print(transport)  # Тип транспорта None марки Telega может развить скорость 10 км/ч
# bike = Transport('shkolnik', 20, 'bike')
# print(bike)  # Тип транспорта bike марки shkolnik может развить скорость 20 км/ч
#
# first_plane = Plane('Virgin Atlantic', 700, 450)
# print(first_plane)  # Самолет марки Virgin Atlantic вмещает в себя 450 людей
# first_car = Car('BMW', 230, 75000, 300)
# print(first_car)  # Тип транспорта Car марки BMW может развить скорость 230 км/ч
# print(first_car.gasoline)  # Осталось бензина на 300 км
# first_car.gasoline = 20  # Печатает 'Объем топлива увеличен на 20 л и составляет 320 л'
# print(first_car.gasoline)  # Осталось бензина на 320 км
# second_car = Car('Audi', 230, 70000, 130)
# second_car.gasoline = [None]  # Печатает 'Ошибка заправки автомобиля'
# first_boat = Boat('Yamaha', 40, 'Petr')
# print(first_boat)  # Этой лодкой марки Yamaha владеет Petr


class Initialization:
    def __init__(self, capacity, food):
        if not isinstance(capacity, int):
            print('Количество людей должно быть целым числом')
        else:
            self.capacity = capacity
            self.food = food


class Vegetarian(Initialization):
    def __init__(self, capacity, food):
        super().__init__(capacity, food)

    def __str__(self):
        return f"{self.capacity} людей предпочитают не есть мясо! Они предпочитают {self.food}"


class MeatEater(Initialization):
    def __init__(self, capacity, food):
        super().__init__(capacity, food)

    def __str__(self):
        return f"{self.capacity} мясоедов в Москве! Помимо мяса они едят еще и {self.food}"


class SweetTooth(Initialization):
    def __init__(self, capacity, food):
        super().__init__(capacity, food)

    def __str__(self):
        return f"Сладкоежек в Москве {self.capacity}. Их самая любимая еда: {self.food}"

    def __eq__(self, other):
        if not isinstance(other, (int, Initialization)):
            return f"Невозможно сравнить количество сладкоежек с {other}"
        else:
            if (isinstance(other, int) and other == self.capacity) or (
                    isinstance(other, Initialization) and other.capacity == self.capacity):
                return True
            else:
                return False

    def __lt__(self, other):
        if not isinstance(other, (int, Initialization)):
            return f"Невозможно сравнить количество сладкоежек с {other}"
        else:
            if (isinstance(other, int) and other > self.capacity) or (
                    isinstance(other, Initialization) and other.capacity > self.capacity):
                return True
            else:
                return False

    def __gt__(self, other):
        if not isinstance(other, (int, Initialization)):
            return f"Невозможно сравнить количество сладкоежек с {other}"
        else:
            if (isinstance(other, int) and other < self.capacity) or (
                    isinstance(other, Initialization) and other.capacity < self.capacity):
                return True
            else:
                return False


v_first = Vegetarian(10000, ['Орехи', 'овощи', 'фрукты'])
print(v_first)  # 10000 людей предпочитают не есть мясо! Они предпочитают ['Орехи', 'овощи', 'фрукты']
v_second = Vegetarian([23], ['nothing'])  # Количество людей должно быть целым числом
m_first = MeatEater(15000, ['Жареную картошку', 'рыба'])
print(m_first)  # 15000 мясоедов в Москве! Помимо мяса они едят еще и ['Жареную картошку', 'рыба']
s_first = SweetTooth(30000, ['Мороженое', 'Чипсы', 'ШОКОЛАД'])
print(s_first)  # Сладкоежек в Москве 30000. Их самая любимая еда: ['Мороженое', 'Чипсы', 'ШОКОЛАД']
print(s_first > v_first)  # True
print(30000 == s_first)  # True
print(s_first == 25000)  # False
print(100000 < s_first)  # False
print(100 < s_first)  # True
