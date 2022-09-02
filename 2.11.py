# property practice

from string import digits


class User:
    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.__secret = 'fsadfasdf'

    @property
    def secret(self):
        s = input('input your password')
        if s == self.password:
            return self.secret
        else:
            raise ValueError('access denied')

    @property
    def password(self):
        print('getter')
        return self.__password

    @staticmethod
    def is_include_number(password):
        for digit in digits:
            if digit in password:
                return True
        return False

    @staticmethod
    def is_in_blacklist(password):
        with open('2.11.passwords.txt', 'r', encoding='utf-8') as file:
            for line in file:
                if password == line.strip():
                    return True
            return False

    @password.setter
    def password(self, value):
        print('setter')
        if not isinstance(value, str):
            raise TypeError('password must be a string')
        if len(value) < 4 or len(value) > 12:
            raise ValueError('password len must be from 4 to 12 symbols')
        if not User.is_include_number(value):
            raise ValueError('password must have 1 digit')
        if User.is_in_blacklist(value):
            raise ValueError('password is in blacklist')
        self.__password = value


# q = User('ivan', 'pass435')
#
# print(q.password)
#
# q.password = '123qwerty'
#
# print(q.password)


class Registration:
    def __init__(self, login):
        self.login = login

    @staticmethod
    def has_symbol(value, symbol):
        if symbol in value:
            return True
        return False

    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, value):
        if not Registration.has_symbol(value, '@'):
            raise ValueError("Логин должен содержать один символ '@'")

        if not Registration.has_symbol(value, '.'):
            raise ValueError("Логин должен содержать символ '.'")

        if value.find('@') < value.find('.'):
            raise ValueError("Говёный email - как можно записать такой логин?")

        else:
            self.__login = value


# r1 = Registration('qwerty@rambler.ru')  # здесь хороший логин
# print(r1.login)  # qwerty@rambler.ru

# # теперь пытаемся запись плохой логин
# r1.login = '123456'  # ValueError("Логин должен содержать один символ '@'")

# r2 = Registration('qwerty.ru')  # ValueError("Логин должен содержать один символ '@'")
# r3 = Registration('qwerty@ru')  # ValueError("Логин должен содержать символ '.'")
