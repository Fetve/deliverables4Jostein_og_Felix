import pytest

from temperature import Temperature

# A small tolerance constant is available for approximate numeric comparisons.
TOL  = 1e-9

# Initialization tests
def test_default_unit():
    # A temperature given without a unit should default to Celsius.
    assert Temperature(25).unit == "C"

def test_case_insensitive_unit():
    # Unit letters should be accepted regardless of their letter case.
    assert Temperature(25, "c").unit == "C"
    assert Temperature(25, "f").unit == "F"
    assert Temperature(25, "k").unit == "K"


def test_read_only():
    # Temperature values and units must not be changed after construction.
    t = Temperature(25, "C")
    with pytest.raises(AttributeError):
        t.value = 30
    with pytest.raises(AttributeError):
        t.unit = "F"

# Validation
def test_invalid_unit():
    # Any unit other than Celsius, Fahrenheit, or Kelvin is invalid.
    with pytest.raises(ValueError):
        Temperature(25, "X")

def test_below_abs_zero():
    # Each unit must reject values below its absolute-zero threshold.
    with pytest.raises(ValueError):
        Temperature(-274, "C")
    with pytest.raises(ValueError):
        Temperature(-460, "F")
    with pytest.raises(ValueError):
        Temperature(-1, "K")

# Conversions
def check(c, f, k):
    # Create a Celsius temperature and verify the expected values in all units.
    t = Temperature(c, "C")
    assert t.to_fahrenheit() == pytest.approx(f)
    assert t.to_kelvin() == pytest.approx(k)
    # A temperature in Fahrenheit or Kelvin should convert back to Celsius.
    assert Temperature(f, "F").to_celsius() == pytest.approx(c)
    assert Temperature(k, "K").to_celsius() == pytest.approx(c)

def test_abs_zero():
    # Absolute zero is 0 K, -273.15 degrees Celsius, and -459.67 degrees Fahrenheit.
    check(-273.15, -459.67, 0)

def test_crossover():
    # Celsius and Fahrenheit meet at -40 degrees.
    check(-40, -40, 233.15)

def test_freezing_water():
    # Check the freezing point of water in the three temperature units.
    check(0, 32, 273.15)

def test_body_temp():
    # Check an approximate normal body temperature.
    check(37, 98.6, 310.15)

def test_boiling():
    # Check the boiling point of water in the three temperature units.
    check(100, 212, 373.15)

# Round Trip
def test_round_trip():
    # Converting through Fahrenheit and Kelvin should return the original temperature.
    t = Temperature(25, "C")
    assert t.convert_to("F").convert_to("K").convert_to("C") == t

# Cross-unit comparison
def test_equality():
    # Equivalent temperatures expressed in different units compare as equal.
    assert Temperature(0, "C") == Temperature(32, "F")
    assert Temperature(0, "C") == Temperature(273.15, "K")
    assert Temperature(0, "C") <= Temperature(32, "F")
    assert Temperature(0, "C") >= Temperature(32, "F")

def test_ordering():
    # Ordering comparisons should also use the temperatures' Celsius values.
    a = Temperature(0, "C")
    b = Temperature(50, "F") # 10 deg celsius
    assert a < b
    assert a <= b
    assert b > a
    assert b >= a
    # The opposite direction must be False.
    assert not (b < a)
    assert not (a > b)

# Formatting
def test_str():
    # The string format should include two decimal places and a degree symbol.
    assert str(Temperature(25, "C")) == "25.00 °C"

def test_repr():
    # The representation should show the value and unit in constructor format.
    assert repr(Temperature(25, "C")) == "Temperature(25.0, 'C')"
