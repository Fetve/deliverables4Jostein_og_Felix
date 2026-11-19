from math import isclose

# Define the Temperature class and validate input values.

class Temperature:
    def __init__(self, value, unit="C") -> None:
        # Accept units regardless of letter case and normalize them to uppercase.
        unit = unit.upper()

        # Store private values so that properties can make them read-only.
        self._value = value
        self._unit = unit

        # Reject unsupported units and temperatures below absolute zero.
        if unit not in {"C", "F", "K"}:
            raise ValueError("Invalid unit. Please use 'C', 'F', or 'K'.")
        elif unit == "K" and value < 0:
            raise ValueError("Temperature in Kelvin cannot be negative.")
        elif unit == "C" and value < -273.15:
            raise ValueError("Temperature in Celsius cannot be below -273.15.")
        elif unit == "F" and value < -459.67:
            raise ValueError("Temperature in Fahrenheit cannot be below -459.67.")

    # Expose the stored value without allowing it to be changed directly.
    @property
    def value(self) -> float:
        return self._value

    # Expose the normalized unit without allowing it to be changed directly.
    @property
    def unit(self) -> str:
        return self._unit

# Convert temperatures between Celsius, Fahrenheit, and Kelvin.

    def to_celsius(self) -> float:
        # Celsius values remain unchanged.
        if self.unit == "C":
            return self.value
        # Convert Fahrenheit to Celsius.
        elif self.unit == "F":
            return (self.value - 32) * 5 / 9
        # Convert Kelvin to Celsius.
        elif self.unit == "K":
            return self.value - 273.15
        else:
            raise ValueError("Invalid unit. Please use 'C', 'F', or 'K'.")

    def to_fahrenheit(self) -> float:
        # Convert Celsius to Fahrenheit.
        if self.unit == "C":
            return (self.value * 9 / 5) + 32
        # Fahrenheit values remain unchanged.
        elif self.unit == "F":
            return self.value
        # Convert Kelvin to Fahrenheit.
        elif self.unit == "K":
            return (self.value - 273.15) * 9 / 5 + 32
        else: 
            raise ValueError("Invalid unit. Please use 'C', 'F', or 'K'.")

    def to_kelvin(self) -> float:
        # Convert Celsius to Kelvin.
        if self.unit == "C":
            return self.value + 273.15
        # Convert Fahrenheit to Kelvin.
        elif self.unit == "F":
            return (self.value - 32) * 5 / 9 + 273.15
        # Kelvin values remain unchanged.
        elif self.unit == "K":
            return self.value
        else:
            raise ValueError("Invalid unit. Please use 'C', 'F', or 'K'.")

    def convert_to(self, target_unit: str) -> Temperature:
        target_unit = target_unit.upper()
        # Reject conversion targets outside the supported unit set.
        if target_unit not in {"C", "F", "K"}:
            raise ValueError("Invalid target unit. Please use 'C', 'F', or 'K'.")
        
        # Create a new Temperature object in the requested unit.
        if target_unit == "C":
            return Temperature(self.to_celsius(), "C")
        elif target_unit == "F":
            return Temperature(self.to_fahrenheit(), "F")
        elif target_unit == "K":
            return Temperature(self.to_kelvin(), "K")
        else:
            raise ValueError("Invalid target unit. Please use 'C', 'F', or 'K'.")

# Format Temperature objects as strings.

    def __repr__(self) -> str:
        # Return the constructor-style representation.
        return f"Temperature({float(self.value)!r}, '{self.unit}')"

    def __str__(self) -> str:
        # Display the value with two decimals and the degree symbol.
        if self.unit == "C":
            return f"{self.value:.2f} °C"
        elif self.unit == "F":
            return f"{self.value:.2f} °F"
        else:  
            return f"{self.value:.2f} K"

# Compare temperatures while accounting for their original units.

    def __eq__(self, other: object):
        # Only temperatures can be compared; compare Celsius values approximately.
        if not isinstance(other, Temperature):
            return NotImplemented
        return isclose(
            self.to_celsius(), other.to_celsius(), rel_tol=0.0, abs_tol=1e-9
        )

    def __ne__(self, other: object):
        # Inequality is the opposite of equality.
        if not isinstance(other, Temperature):
            return NotImplemented
        return not self == other

    def __lt__(self, other: object):
        # Strictly lower: lower AND not equal within the 1e-9 tolerance.
        # 'and self != other' stops two temperatures that count as equal 
        # from being considered lower or higher than each other.
        if not isinstance(other, Temperature):
            return NotImplemented
        return self.to_celsius() < other.to_celsius() and self != other

    def __le__(self, other: object):
        # Lower OR equal. We use '<', not '<=' for the 'lower' part, and let
        # 'self == other' handle the 'equal' part. That way equality uses the
        # 1e-9 tolerance from __eq__, so <= always agrees with ==.
        # A plain '<=' would say 1e-10 C <= 0 C is False, even though they are equal.
        if not isinstance(other, Temperature):
            return NotImplemented
        return self.to_celsius() < other.to_celsius() or self == other

    def __gt__(self, other: object):
        # Strictly higher: higher AND not equal within the 1e-9 tolerance.
        if not isinstance(other, Temperature):
            return NotImplemented
        return self.to_celsius() > other.to_celsius() and self != other

    def __ge__(self, other: object):
        # Higher OR equal. Same idea as __le__: '>' for the 'higher' part, and
        # 'self == other' for the 'equal' part, so the tolerance is used.
        if not isinstance(other, Temperature):
            return NotImplemented
        return self.to_celsius() > other.to_celsius() or self == other
