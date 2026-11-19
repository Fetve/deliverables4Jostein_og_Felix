from math import gcd


class Fraction:
    def __init__(self, numerator: int, denominator = 1):
        # Both parts of a fraction must be integers.
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError("Numerator and Denominator must be integers.")

        # A denominator of zero would make the fraction undefined.
        if denominator == 0:
            raise ZeroDivisionError("Denominator cannot be == 0.")

        # Normalize the sign so that negative fractions have a negative numerator.
        if denominator < 0:
            numerator = -numerator
            denominator = -denominator

        # Reduce the fraction by dividing by the greatest common divisor.
        common = gcd(numerator, denominator)
        self.numerator = numerator // common
        self.denominator = denominator // common

    def __repr__(self):
        # Provide a representation that identifies the class and constructor values.
        return f"Fraction({self.numerator}, {self.denominator})"

    def __str__(self):
        # Display the fraction in numerator/denominator form.
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        # Addition is supported only when the other value is a Fraction.
        if not isinstance(other, Fraction):
            return NotImplemented
        # Find a common denominator, then add the adjusted numerators.
        return Fraction(self.numerator * other.denominator + other.numerator * self.denominator, self.denominator * other.denominator)

    def __sub__(self, other):
        # Subtraction is supported only when the other value is a Fraction.
        if not isinstance(other, Fraction):
            return NotImplemented
        # Find a common denominator, then subtract the adjusted numerators.
        return Fraction(self.numerator * other.denominator - other.numerator * self.denominator, self.denominator * other.denominator)

    def __mul__(self, other):
        # Multiplication is supported only when the other value is a Fraction.
        if not isinstance(other, Fraction):
            return NotImplemented
        # Multiply the numerators together and the denominators together.
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)

    def __truediv__(self, other):
        # Division is supported only when the other value is a Fraction.
        if not isinstance(other, Fraction):
            return NotImplemented
        # Divide by multiplying by the reciprocal of the second fraction.
        return Fraction(self.numerator * other.denominator, self.denominator * other.numerator)


    def __eq__(self, other):
        # Compare the fractions using cross-multiplication.
        if not isinstance(other, Fraction):
            return NotImplemented
        return self.numerator * other.denominator == self.denominator * other.numerator

    def __ne__(self, other):
        # Two fractions are unequal when their cross-products differ.
        if not isinstance(other, Fraction):
            return NotImplemented
        return self.numerator * other.denominator != self.denominator * other.numerator
    
    def __lt__(self, other):
        # Compare whether this fraction is less than the other fraction.
        if not isinstance(other, Fraction):
            return NotImplemented
        return self.numerator * other.denominator < self.denominator * other.numerator
    
    def __le__(self, other):
        # Compare whether this fraction is less than or equal to the other fraction.
        if not isinstance(other, Fraction):
            return NotImplemented
        return self.numerator * other.denominator <= self.denominator * other.numerator
    
    def __gt__(self, other):
        # Compare whether this fraction is greater than the other fraction.
        if not isinstance(other, Fraction):
            return NotImplemented
        return self.numerator * other.denominator > self.denominator * other.numerator
    
    def __ge__(self, other):
        # Compare whether this fraction is greater than or equal to the other fraction.
        if not isinstance(other, Fraction):
            return NotImplemented
        return self.numerator * other.denominator >= self.denominator * other.numerator
    