class Fraction(object):

    def __init__(self, num, den):
        self.__num = num
        self.__den = den
        self.reduce()

    def __str__(self):
        return '%d/%d' % (self.__num, self.__den)

    def __neg__(self):
        return Fraction(-self.__num, self.__den)

    def __invert__(self):
        return Fraction(self.__den, self.__num)

    def __pow__(self, power, modulo=None):
        return Fraction(self.__num ** 2, self.__den ** 2)

    def __float__(self):
        return self.__num / self.__den

    def __int__(self):
        return int(float(self))

    def reduce(self):
        g = Fraction.gcd(self.__num, self.__den)
        self.__num /= g
        self.__den /= g

    @staticmethod
    def gcd(n, m):
        if m == 0:
            return n
        else:
            return Fraction.gcd(m, n % m)


frac = Fraction(7, 2)
print(-frac)
print(~frac)
print(frac**2)
print(float(frac))
print(int(frac))

#Complete
