# public, private, protected attr and methods

class BankAccount:
    def __init__(self, name, balance, passport):
        self.__name = name
        self.__balance = balance
        self.__passport = passport

    def print_public_data(self):
        self.__print_private_data()

    def print_protected_data(self):
        print(self._name, self._balance, self._passport)

    def __print_private_data(self):
        print(self.__name, self.__balance, self.__passport)


# account1 = BankAccount('Bob', 100000, 34234234234)
# account1.print_public_data()
#
# print(account1._BankAccount__balance)
#
# print(dir(account1))


# print(account1.__name)
# print(account1.__balance)
# print(account1.__passport)

# ---

class Student:
    def __init__(self, name, age, branch):
        self.__name = name
        self.__age = age
        self.__branch = branch

    def __display_details(self):
        print(f'''
            Имя: {self.__name}
            Возраст: {self.__age}
            Направление: {self.__branch}
        ''')

    def access_private_method(self):
        self.__display_details()

#
# obj = Student("Adam Smith", 25, "Information Technology")
# obj.access_private_method()


# ---

