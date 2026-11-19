# Deliverable 4 – INF201 (Jostein og Felix)

GitHub repository: https://github.com/Fetve/deliverables4Jostein_og_Felix

## Contents

| File | Description |
|---|---|
| `temperature.py` | Task 1: `Temperature` class supporting Celsius, Fahrenheit and Kelvin |
| `test_temperature.py` | Task 1: pytest tests for `Temperature` (15 tests) |
| `fraction.py` | Task 2: `Fraction` class with comparisons and arithmetic special methods |
| `test_fraction.py` | Task 2: pytest tests for `Fraction` (16 tests) |
| `deliverable_4_solution.ipynb` | Notebook with the test output for both tasks |
| `deliverable_4.ipynb` | The assignment text |
| `requirements.txt` | Packages in the virtual environment |

## Discussion: Use of AI

We used Claude (Anthropic) as a programming assistant during this deliverable.

**Task 1 (Temperature):** We wrote the first version of the class ourselves and asked Claude to review it against the assignment. It pointed out missing requirements: a default unit, case-insensitive units (also in `convert_to`), read-only `value`/`unit` properties, the comparison methods, and a `__repr__` that does not round the value. It also helped us find bugs in `__le__` and `__ge__`, and explained why they use `<` together with `or self == other` so that the 1e-9 tolerance is respected. Claude suggested which tests to write, and we based `test_temperature.py` on a minimal example from it.

**Task 2 (Fraction):** We wrote our own version and used Claude to check it, for example that a zero denominator should raise `ZeroDivisionError` rather than `TypeError`.

**Other help:** Explanations of dunder methods, `pip freeze`/`requirements.txt` and `.gitignore`, and adding explanatory comments to the code.

**Checking:** All suggestions were reviewed by us, and we verified the code by running the test suites (31 tests, all passing).

**Reflection:** We learned how to be better at problem solving with help from AI, and how
easy it is to miss small errors. For example, our `__le__` and `__ge__` methods looked
correct, but returned the wrong result for equal temperatures, and our tests did not
catch it until we added a test for that case. This showed us that tests should also check
edge cases and the "opposite" direction, not only the expected result.