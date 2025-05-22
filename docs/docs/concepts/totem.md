---
sidebar_position: 2
---

# Totem

The `Totem` class represents a Minecraft totem texture generated from a skin. It provides methods for scaling and saving the totem image.

## Overview

After a totem is built using the `TotemBuilder`, the result is a `Totem` object. This object contains the generated totem image and provides methods to manipulate it, such as scaling it to a larger size while preserving the pixel art quality.

## Properties

The `Totem` class has the following properties:

- `image`: The PIL Image object representing the totem texture
- `slim`: Boolean indicating whether the totem was created from a slim skin
- `style`: The style class used to create the totem
- `rounded_head`: Boolean indicating whether the head is rounded
- `top_layers`: List of TopLayer enum values indicating which parts have second layers applied

## Methods

### scale

The `scale` method scales the totem image by a given factor without losing quality:

```python
def scale(self, *, factor: int) -> Image.Image:
    """
    Scale method scales an image by a given factor.

    :param factor: The factor by which the image will be scaled. Must be greater than 0.
    :rtype factor: int
    :return: The scaled image as an instance of Image from PIL.

    :raises SmallScale: If the scale factor is less than or equal to 0.
    """
```

Example usage:

```python
from wavy_totem_lib import TotemBuilder, Skin

# Create and build a totem
totem = TotemBuilder(Skin('my_skin.png')).build()

# Scale the totem by a factor of 8 (from 16x16 to 128x128)
scaled_image = totem.scale(factor=8)

# Save the scaled image
scaled_image.save('scaled_totem.png')
```

### save

While not a direct method of the `Totem` class, you can save the totem image using the PIL Image's `save` method:

```python
# Save the totem image
totem.image.save('totem.png')

# Save with specific format and options
totem.image.save('totem.png', format='PNG', optimize=True)
```

## Why Use the scale Method?

The `scale` method is specifically designed for pixel art scaling. Unlike PIL's `resize` method, which can introduce blurring or interpolation artifacts, the `scale` method performs a pixel-perfect scaling that preserves the sharp edges and pixelated look of Minecraft textures.

Each pixel in the original image is expanded to a square of pixels in the scaled image, ensuring that the scaled image looks like a larger version of the original without any quality loss.

## Example: Scaling a Totem

Here's a complete example of creating a totem and scaling it to different sizes:

```python
from wavy_totem_lib import TotemBuilder, Skin

# Create a builder
builder = TotemBuilder(Skin('my_skin.png'))

# Build the totem
totem = builder.build()

# Save the original 16x16 totem
totem.image.save('totem_16x16.png')

# Scale and save at different sizes
totem.scale(factor=2).save('totem_32x32.png')
totem.scale(factor=4).save('totem_64x64.png')
totem.scale(factor=8).save('totem_128x128.png')
```

This will create four versions of the totem at different sizes: 16x16 (original), 32x32, 64x64, and 128x128.

## Error Handling

The `scale` method will raise a `SmallScale` exception if you try to scale by a factor less than or equal to 0:

```python
try:
    # This will raise a SmallScale exception
    totem.scale(factor=0)
except SmallScale:
    print("Scale factor must be greater than 0")
```

## Usage in Workflows

The `Totem` class is typically the final result of the totem generation process:

1. Create a `Skin` object from a skin file
2. Use a `TotemBuilder` to build a `Totem` from the skin
3. Scale the totem to the desired size
4. Save or further process the totem image

This workflow is demonstrated in the [Getting Started](../getting-started.mdx) and [Examples](../examples.md) sections.