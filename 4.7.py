# MRO

class O:
    pass


class A(O):
    pass


class B(O):
    pass


class C(O):
    pass


class D(O):
    pass


class E(O):
    pass


class K1(C, A, B):
    pass


class K2(A, D):
    pass


class K3(B, D, E):
    pass


class Z(K1, K2, K3):
    pass


def get_mro(cls):
    print(*[c.__name__ for c in cls.mro()], sep=' -> ')  # usable print classes MRO line


get_mro(Z)


# ERRORS:

class X:
    pass
class Y:
    pass
class A(X, Y):
    pass
class B(Y, X):
    pass
class G(A, B):
    pass

# get_mro(G)

# TypeError: Cannot create a consistent method resolution
# order (MRO) for bases X, Y

class X:
    pass
class Y(X):
    pass
class A(X, Y):
    pass

get_mro(A)
