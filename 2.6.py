# property, setters and getters

class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def get_balance(self):  # getter
        print('getter')
        return self.__balance

    def set_balance(self, value):  # setter
        print('setter')
        if not isinstance(value, (int, float)):
            raise ValueError('balance must be a numeric')
        self.__balance = value

    def delete_balance(self):  # delete attribute
        print('delete')
        del self.__balance

    balance = property(fget=get_balance, fset=set_balance, fdel=delete_balance)  # property


#
# b = BankAccount('ivan', 1000)
# b.balance = 999999900
# print(b.balance)
# del b.balance
# b.balance = 33434343
# print(b.balance)


# ---

class Person:
    def __init__(self, name):
        self._name = name

    def _get_name(self):
        print("Get name")
        return self._name

    def _set_name(self, value):
        print("Set name")
        self._name = value

    def _del_name(self):
        print("Delete name")
        del self._name

    name = property(
        fget=_get_name,
        fset=_set_name,
        fdel=_del_name,
        doc="The name property."
    )


# ---

class UserMail:
    def __init__(self, login, email):
        self.login = login
        self.__email = email

    def get_email(self):
        return self.__email

    def set_email(self, value):  # email check
        if ('@' in value) \
                and ('.' in value) \
                and (value.find('@') < value.find('.')) \
                and (value.count('@') == 1) \
                and (value.count('.') == 1):
            self.__email = value
        else:
            print(f"ErrorMail:{value}")

    email = property(
        fget=get_email,
        fset=set_email
    )
