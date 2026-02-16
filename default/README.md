# Example555 Math Operations

This repository implements basic math operations (addition and subtraction) in Python with comprehensive pytest-based tests.

## Structure

- `src/` : Production code for math operations
- `tests/` : Pytest test cases for addition and subtraction
- `default/requirements.txt` : Dependency list
- `default/math.json` : CI workflow metadata

## Usage

To use the math operations:

```
from src.math_operations import add, subtract
result = add(2, 3)
result2 = subtract(5, 1)
```

## Running Tests

Install dependencies:

```
pip install -r default/requirements.txt
```

Run all tests:

```
pytest tests/
```

## CI/CD Workflow

GitHub Actions workflow is described in `default/math.json` and will run tests for each push to the `Feature1` branch.
