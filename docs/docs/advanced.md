---
sidebar_position: 6
---

# Advanced Topics

This section covers advanced topics for users who want to go beyond the basic functionality of wavy-totem-lib.

## Creating Custom Styles

While wavy-totem-lib comes with built-in styles (WavyStyle and STTStyle), you might want to create your own style for a unique look. Here's a more detailed guide on creating custom styles:

### Basic Structure

A custom style must inherit from `AbstractStyle` and implement the `image` property:

```python
from PIL import Image
from wavy_totem_lib.styles.abstract import AbstractStyle
from wavy_totem_lib.options import TopLayer
from wavy_totem_lib.skin import Skin

class MyCustomStyle(AbstractStyle):
    def __init__(self, skin: Skin, top_layers: list[TopLayer], **kwargs):
        super().__init__(skin, top_layers, **kwargs)
        # You can initialize additional attributes here

    @property
    def image(self) -> Image.Image:
        # Implement your style logic here
        # Use self.skin to access the skin parts
        # Use self._canvas to build the totem image
        return self._canvas
```

### Adding Custom Parameters

You can add custom parameters to your style by accepting them in the `__init__` method and storing them as attributes:

```python
def __init__(self, skin: Skin, top_layers: list[TopLayer], **kwargs):
    super().__init__(skin, top_layers, **kwargs)
    self.custom_param = kwargs.get('custom_param', default_value)
```

Then you can use these parameters in your `image` property:

```python
@property
def image(self) -> Image.Image:
    if self.custom_param:
        # Do something special
    else:
        # Do the default behavior
    return self._canvas
```

### Using the Custom Style

To use your custom style, pass it to the `TotemBuilder`:

```python
from wavy_totem_lib import TotemBuilder, Skin
from my_module import MyCustomStyle

builder = TotemBuilder(
    Skin('my_skin.png'),
    style=MyCustomStyle,
    # If your style accepts custom parameters:
    # These will be passed as kwargs to your style's __init__ method
)

# If your style accepts custom parameters, you can also pass them here:
totem = builder.build(custom_param=value)
```

## Error Handling

wavy-totem-lib can raise several exceptions that you might want to handle in your code:

### SmallScale Exception

The `SmallScale` exception is raised when you try to scale a totem with a factor less than or equal to 0:

```python
from wavy_totem_lib import TotemBuilder, Skin
from wavy_totem_lib.exceptions import SmallScale

try:
    totem = TotemBuilder(Skin('my_skin.png')).build()
    scaled = totem.scale(factor=0)  # This will raise SmallScale
except SmallScale:
    print("Scale factor must be greater than 0")
```

### File Not Found

If the skin file doesn't exist, a `FileNotFoundError` will be raised:

```python
from wavy_totem_lib import Skin

try:
    skin = Skin('non_existent_file.png')
except FileNotFoundError:
    print("Skin file not found")
```

### Invalid Skin Format

If the skin file is not a valid image or has an invalid format, a `PIL.UnidentifiedImageError` might be raised:

```python
from PIL import UnidentifiedImageError
from wavy_totem_lib import Skin

try:
    skin = Skin('invalid_image.txt')
except UnidentifiedImageError:
    print("Invalid image format")
```

## Performance Optimization

If you're generating many totems, consider these optimization techniques:

### Asynchronous Generation

Use the `build_async` method to generate totems asynchronously:

```python
import asyncio
from wavy_totem_lib import TotemBuilder, Skin

async def generate_many_totems(skin_files):
    results = []
    for skin_file in skin_files:
        builder = TotemBuilder(Skin(skin_file))
        totem = await builder.build_async()
        results.append(totem)
    return results

# Run the async function
totems = asyncio.run(generate_many_totems(['skin1.png', 'skin2.png', 'skin3.png']))
```

### Reusing Skin Objects

If you need to generate multiple totems with different styles for the same skin, reuse the `Skin` object:

```python
from wavy_totem_lib import TotemBuilder, Skin, WavyStyle, STTStyle

skin = Skin('my_skin.png')

# Generate totems with different styles
wavy_totem = TotemBuilder(skin, style=WavyStyle).build()
stt_totem = TotemBuilder(skin, style=STTStyle).build()
```

## Working with BytesIO

If you're working with web applications or want to avoid writing to disk, you can use `BytesIO`:

```python
from io import BytesIO
from PIL import Image
from wavy_totem_lib import TotemBuilder, Skin

# Load skin from BytesIO
skin_bytes = BytesIO(skin_data)  # skin_data could come from a web request
skin = Skin(skin_bytes)

# Generate totem
totem = TotemBuilder(skin).build()

# Save totem to BytesIO
output = BytesIO()
totem.image.save(output, format='PNG')
output.seek(0)

# Now you can use output.getvalue() to get the bytes
# or pass output to another function that accepts file-like objects
```

These advanced techniques should help you get the most out of wavy-totem-lib for your specific use case.