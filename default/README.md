# Math Operations Example

This repository implements basic math operations (addition and subtraction) with production-ready Python code and comprehensive tests using pytest.

## Folder Structure

- `src/` : Source code for math operations
- `tests/` : Test cases for math operations
- `default/requirements.txt` : Python dependencies
- `default/math.json` : CI/CD workflow metadata for automation agents

## Usage

```
from src.math_operations import add, subtract

print(add(2, 3))        # Output: 5
print(subtract(5, 2))   # Output: 3
```

## Running Tests

Install dependencies:

```
pip install -r default/requirements.txt
```

Run tests:

```
pytest tests/
```

## CI/CD Workflow

See `.github/workflows/ci.yml` (generated via metadata in `default/math.json`).
