---
sidebar_position: 7
---

# Contributing

This guide provides information for developers who want to contribute to wavy-totem-lib.

## Development Setup

To set up the development environment:

1. Clone the repository:
   ```bash
   git clone https://github.com/wavy-cat/wavy-totem-lib.git
   cd wavy-totem-lib
   ```

2. Install dependencies:
   ```bash
   pip install -e ".[dev]"
   ```

## Project Structure

The project is organized as follows:

- `wavy_totem_lib/`: Main package directory
  - `styles/`: Contains style implementations
    - `abstract.py`: Abstract base class for styles
    - `wavy.py`: WavyStyle implementation
    - `soul.py`: STTStyle implementation
  - `skin.py`: Skin class implementation
  - `totem.py`: Totem class implementation
  - `builder.py`: TotemBuilder class implementation
  - `options.py`: TopLayer enum and other options
  - `exceptions.py`: Custom exceptions

## Coding Standards

- Follow PEP 8 style guidelines
- Use type hints for function parameters and return values
- Write docstrings for all public classes and methods
- Keep the code simple and readable

## Adding a New Style

To add a new style:

1. Create a new file in the `wavy_totem_lib/styles/` directory
2. Define a class that inherits from `AbstractStyle`
3. Implement the `__init__` and `image` methods
4. Add the style to the public API in `__init__.py`

Example:

```python
from PIL import Image
from .abstract import AbstractStyle
from ..options import TopLayer
from ..skin import Skin

class MyNewStyle(AbstractStyle):
    def __init__(self, skin: Skin, top_layers: list[TopLayer], **kwargs):
        super().__init__(skin, top_layers, **kwargs)
        # Custom initialization

    @property
    def image(self) -> Image.Image:
        # Implement your style logic here
        # ...
        return self._canvas
```

## Testing

Before submitting a pull request, make sure to:

1. Run the tests:
   ```bash
   pytest
   ```

2. Check code style:
   ```bash
   flake8
   ```

3. Verify type hints:
   ```bash
   mypy wavy_totem_lib
   ```

## Pull Request Process

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests and ensure they pass
5. Submit a pull request

## License

By contributing to wavy-totem-lib, you agree that your contributions will be licensed under the project's license (Boost Software License, Version 1.0).