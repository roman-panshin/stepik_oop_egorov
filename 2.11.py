# property practice

# from string import digits, ascii_letters


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

# ---

from string import digits, ascii_letters


class Registration:
    def __init__(self, login, password):
        self.login = login
        self.password = password

    @staticmethod
    def has_symbol(value, symbol):
        if symbol in value:
            return True
        return False

    @staticmethod
    def is_include_digit(value):
        flag = False
        for i in value:
            if i in digits:
                flag = True
        return flag

    @staticmethod
    def is_include_all_register(value):
        if value != value.lower() and value != value.upper():
            return True
        return False

    @staticmethod
    def is_include_only_latin(value):
        flag = False
        for i in value:
            if i in ascii_letters:
                flag = True
        return flag

    @staticmethod
    def check_password_dictionary(value, dict):
        with open(dict, 'r', encoding='utf-8') as file:
            for line in file:
                if value == line.strip():
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

        if value.find('@') > value.find('.'):
            raise ValueError("Говёный email - как можно записать такой логин?")

        else:
            self.__login = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        if not isinstance(value, str):
            raise TypeError("Пароль должен быть строкой")

        if not 4 < len(value) < 12:
            raise ValueError('Пароль должен быть длиннее 4 и меньше 12 символов')

        if not Registration.is_include_digit(value):
            raise ValueError('Пароль должен содержать хотя бы одну цифру')

        if not Registration.is_include_all_register(value):
            raise ValueError('Пароль должен содержать хотя бы один символ верхнего и нижнего регистра')

        if not Registration.is_include_only_latin(value):
            raise ValueError('Пароль должен содержать только латинский алфавит')

        if Registration.check_password_dictionary(value, 'easy_passwords.txt'):
            raise ValueError('Ваш пароль содержится в списке самых легких')

        else:
            self.__password = value


