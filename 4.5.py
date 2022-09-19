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
