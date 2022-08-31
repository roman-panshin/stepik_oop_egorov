# class body scope

# PYTHON_DEV = 1
# GO_DEV = 1
# REACT_DEV = 1


class DepartmentIT:
    PYTHON_DEV = 3
    GO_DEV = 3
    REACT_DEV = 2

    def info(self):
        print(self.PYTHON_DEV, self.GO_DEV, self.REACT_DEV)

    def info2(self):
        print(DepartmentIT.PYTHON_DEV, DepartmentIT.GO_DEV, DepartmentIT.REACT_DEV)

    @property
    def info_prop(self):
        print(self.PYTHON_DEV, self.GO_DEV, self.REACT_DEV)

    @classmethod
    def info_class(cls):
        print(cls.PYTHON_DEV, cls.GO_DEV, cls.REACT_DEV)

    @staticmethod
    def info_static():
        print(DepartmentIT.PYTHON_DEV, DepartmentIT.GO_DEV, DepartmentIT.REACT_DEV)

    def make_backend(self):
        print('Python and Go')

    def make_frontend(self):
        print('React')

    def hiring_python_dev(self):
        self.PYTHON_DEV += 1


it1 = DepartmentIT()


# it1.info()
# it1.info2()
# it1.info_prop
# it1.info_class()
# it1.info_static()

# print(it1.PYTHON_DEV)
# print(it1.__dict__)
# it1.hiring_python_dev()
# print(it1.__dict__)
#
# print(it1.PYTHON_DEV)


# ---


class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role


class Access:
    __access_list = ['admin', 'developer']

    @staticmethod
    def __check_access(user):
        if user.role in Access.__access_list:
            return True
        return False

    @staticmethod
    def get_access(user):
        if not isinstance(user, User):
            print('AccessTypeError')
            return

        if Access.__check_access(user):
            print(f'User {user.name}: success')
        else:
            print('AccessDenied')


user1 = User('batya99', 'admin')
Access.get_access(user1)

zaya = User('milaya_zaya999', 'user')
Access.get_access(zaya)  # печатает AccessDenied

Access.get_access(5)  # печатает AccessTypeError
