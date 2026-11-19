import pytest

from fraction import Fraction


# Initialization tests
def test_init():
    # Create a fraction and verify that it is reduced to its simplest form.
    f = Fraction(2, 4)
    assert f.numerator == 1
    assert f.denominator == 2


def test_negative_denominator():
    # A negative denominator is normalized by moving the sign to the numerator.
    f = Fraction(1, -2)
    assert f.numerator == -1
    assert f.denominator == 2


def test_zero_denominator():
    # Fractions with a denominator of zero must raise an appropriate error.
    with pytest.raises(ZeroDivisionError):
        Fraction(1, 0)


def test_not_integer():
    # Both constructor arguments must be integers.
    with pytest.raises(TypeError):
        Fraction(1.5, 2)


# Comparisons
def test_eq():
    # Equivalent fractions compare as equal even if they have different values.
    assert Fraction(1, 2) == Fraction(2, 4)


def test_ne():
    # Fractions with different numerical values compare as unequal.
    assert Fraction(1, 2) != Fraction(1, 3)


def test_lt():
    # Verify that one fraction is considered less than another.
    assert Fraction(1, 3) < Fraction(1, 2)


def test_le():
    # Verify the less-than-or-equal comparison for unequal and equal fractions.
    assert Fraction(1, 3) <= Fraction(1, 2)
    assert Fraction(1, 2) <= Fraction(1, 2)


def test_gt():
    # Verify that one fraction is considered greater than another.
    assert Fraction(1, 2) > Fraction(1, 3)


def test_ge():
    # Verify the greater-than-or-equal comparison for unequal and equal fractions.
    assert Fraction(1, 2) >= Fraction(1, 3)
    assert Fraction(1, 2) >= Fraction(1, 2)


# Other special methods
def test_add():
    # Adding fractions produces a fraction with the common-denominator result.
    assert Fraction(1, 2) + Fraction(1, 3) == Fraction(5, 6)


def test_sub():
    # Subtracting fractions returns the difference in reduced form.
    assert Fraction(1, 2) - Fraction(1, 3) == Fraction(1, 6)


def test_mul():
    # Multiplying fractions multiplies the numerators and denominators.
    assert Fraction(2, 3) * Fraction(3, 4) == Fraction(1, 2)


def test_truediv():
    # Division is performed by multiplying by the reciprocal of the other fraction.
    assert Fraction(1, 2) / Fraction(1, 4) == Fraction(2, 1)


def test_str():
    # The string representation is displayed as "numerator/denominator".
    assert str(Fraction(3, 4)) == "3/4"


def test_repr():
    # The developer representation identifies the class and both constructor values.
    assert repr(Fraction(3, 4)) == "Fraction(3, 4)"