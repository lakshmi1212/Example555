# Math Operations Example

This repository contains simple math operations (addition and subtraction) with comprehensive pytest-based test coverage.

## Folder Structure

- `src/`: Contains production code (`math_operations.py`).
- `tests/`: Contains test files (`test_add.py`, `test_subtract.py`).
- `default/`: Contains workflow metadata (`math.json`), requirements, and this README.

## Usage

To use the math functions:

```
from src.math_operations import add, subtract
result = add(1, 2)
result2 = subtract(3, 1)
```

## Testing

Install dependencies:

```
pip install -r default/requirements.txt
```

Run tests:

```
pytest tests/
```

## CI Workflow

See `.github/workflows/ci.yml` for automated testing instructions. Workflow metadata is in `default/math.json`.
