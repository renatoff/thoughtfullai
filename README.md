# Package Sorter

A Python package for sorting packages based on dimensions and mass.

## Requirements

- Python 3.12.6
- Dependencies: Install with `pip install -r requirements.txt`

## Running Tests

```bash
python -m pytest
```

## Usage

```python
from src.package_sorter import sort

result = sort(width=10, height=20, length=30, mass=15)
print(result)
```
