import fractions
import sys


class Fraction:
    def __init__(self, top, bottom):
        try:
            if self.is_negative(int(bottom)):
                self.common = -(gcd((int(top)), int(bottom)))
            else:
                self.common = gcd((int(top)), int(bottom))
            self.num = int(top)//self.common
            self.den = int(bottom)//self.common
        except ValueError as e:
            print(e)
            sys.exit(1)

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def is_negative(self, number):
        if number >= 0:
            return False
        return True

    def show(self):
        print(self.num, "/", self.den)

    def __add__(self, other_fraction):
        new_num = self.num * other_fraction.den + \
            self.den * other_fraction.num
        new_den = self.den * other_fraction.den
        if new_num == 0:
            return 0
        elif new_den == 0:
            raise ZeroDivisionError("Cannot divide in zero.")
        else:
            return Fraction(new_num, new_den)

    def __sub__(self, other_fraction):
        new_num = self.num * other_fraction.den - \
            self.den * other_fraction.num
        new_den = self.den * other_fraction.den
        if new_num == 0:
            return 0
        elif new_den == 0:
            raise ZeroDivisionError("Cannot divide in zero.")
        else:
            return Fraction(new_num, new_den)

    def __mul__(self, other_fraction):
        new_num = self.num * other_fraction.num
        new_den = self.den * other_fraction.den
        if new_num == 0:
            return 0
        elif new_den == 0:
            raise ZeroDivisionError("Cannot divide in zero.")
        else:
            return Fraction(new_num, new_den)

    def __truediv__(self, other_fraction):
        new_num = self.num * other_fraction.den
        new_den = self.den * other_fraction.num
        if new_num == 0:
            return 0
        elif new_den == 0:
            raise ZeroDivisionError("Cannot divide in zero.")
        else:
            return Fraction(new_num, new_den)

    def __eq__(self, other):
        first_num = self.num * other.den
        second_num = other.num * self.den
        return first_num == second_num

    def __gt__(self, other):
        first_num = self.num * other.den
        second_num = other.num * self.den
        return first_num > second_num

    def __ge__(self, other):
        first_num = self.num * other.den
        second_num = other.num * self.den
        return first_num >= second_num

    def __lt__(self, other):
        first_num = self.num * other.den
        second_num = other.num * self.den
        return first_num < second_num

    def __le__(self, other):
        first_num = self.num * other.den
        second_num = other.num * self.den
        return first_num <= second_num

    def __ne__(self, other):
        first_num = self.num * other.den
        second_num = other.num * self.den
        return first_num != second_num

    def __radd__(self, other_fraction):
        new_num = self.num * other_fraction.den + \
                  self.den * other_fraction.num
        new_den = self.den * other_fraction.den
        if new_num == 0:
            return 0
        elif new_den == 0:
            raise ZeroDivisionError("Cannot divide in zero.")
        else:
            return Fraction(new_num, new_den)

    def __iadd__(self, other_fraction):
        self = self + other_fraction
        return self

    def get_num(self):
        return self.num

    def get_den(self):
        return self.den


def gcd(m, n):
    while m % n != 0:
        old_m = m
        old_n = n
        m = old_n
        n = old_m % old_n
    return n


f1 = Fraction(3, 4)
f2 = Fraction(2, 5)
print(id(f1))
f1 += f2
print(id(f1))
print(f1)
