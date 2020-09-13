class Fraction:
    def __init__(self, top, bottom):
        self.common = gcd(top, bottom)
        self.num = top//self.common
        self.den = bottom//self.common

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def show(self):
        print(self.num, "/", self.den)

    def __add__(self, other_fraction):
        new_num = self.num * other_fraction.den + \
            self.den * other_fraction.num
        new_den = self.den * other_fraction.den
        return Fraction(new_num, new_den)

    def __eq__(self, other):
        first_num = self.num * other.den
        second_num = other.num * self.den
        return first_num == second_num

    def get_num(self):
        return self.num

    def get_den(self):
        return self.den


def gcd(m, n):
    while m%n != 0:
        old_m = m
        old_n = n
        m = old_n
        n = old_m % old_n
    return n

f1= Fraction(6,8)
