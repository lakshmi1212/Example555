# Math Operations Example

This repository demonstrates simple math operations (addition and subtraction) and includes automated testing using pytest.

## Source Code
- The core logic is in `src/math_operations.py`.

## Tests
- All tests are in the `tests/` folder.
- Run tests using the following command:

```bash
pytest tests/
```

## Requirements
- Python 3.10+
- See `default/requirements.txt` for dependencies.

## CI/CD
- Workflow file: `.github/workflows/ci.yml`
- Test reports are saved to the `reports/` directory (JUnit and HTML).

## Usage

```
from src.math_operations import add, subtract

print(add(2, 3))        # Output: 5
print(subtract(5, 2))   # Output: 3
```
