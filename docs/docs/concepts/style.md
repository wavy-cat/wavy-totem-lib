---
sidebar_position: 4
---

# Styles

Styles in wavy-totem-lib define how a Minecraft skin is transformed into a totem texture. The library comes with
built-in styles and allows you to create custom styles.

## Overview

A style in wavy-totem-lib is a class that inherits from the `AbstractStyle` base class and implements the `image`
property. The style is responsible for taking a `Skin` object and generating a totem texture from it.

## Built-in Styles

wavy-totem-lib comes with two built-in styles:

### WavyStyle

The `WavyStyle` is the default style in wavy-totem-lib. It was created by WavyCat and has been part of the library since
its early versions.

```python
from wavy_totem_lib import TotemBuilder, Skin, WavyStyle

# WavyStyle is the default, so this is optional
builder = TotemBuilder(Skin('my_skin.png'), style=WavyStyle)
```

Here are examples of totems generated with the WavyStyle:

| Notch (wide)                              | WavyCat (slim)                                | CyCeKu (wide)                               |
|-------------------------------------------|-----------------------------------------------|---------------------------------------------|
| ![Notch](@site/static/img/notch_wavy.png) | ![WavyCat](@site/static/img/wavycat_wavy.png) | ![CyCeKu](@site/static/img/cyceku_wavy.png) |

### STTStyle

The `STTStyle` is an alternative style taken from the [UnFamousSoul/STT](https://github.com/UnFamousSoul/STT)
repository.

```python
from wavy_totem_lib import TotemBuilder, Skin, STTStyle

builder = TotemBuilder(Skin('my_skin.png'), style=STTStyle)
```

Here are examples of totems generated with the STTStyle:

| Notch (wide)                             | WavyCat (slim)                               | CyCeKu (wide)                              |
|------------------------------------------|----------------------------------------------|--------------------------------------------|
| ![Notch](@site/static/img/notch_stt.png) | ![WavyCat](@site/static/img/wavycat_stt.png) | ![CyCeKu](@site/static/img/cyceku_stt.png) |

## Creating Custom Styles

You can create your own styles by inheriting from the `AbstractStyle` class and implementing the `image` property.

### The AbstractStyle Class

The `AbstractStyle` class is an abstract base class that defines the interface for all style classes. It has the
following structure:

```python
class AbstractStyle(ABC):
    @abstractmethod
    def __init__(self, skin: Skin, top_layers: list[TopLayer], **kwargs):
        self.skin = skin
        self.top_layers = top_layers
        self.kwargs = kwargs
        self._canvas = Image.new("RGBA", (16, 16))

    @property
    @abstractmethod
    def image(self) -> Image.Image:
        """
        The main method with the @property decorator that generates the totem.
        :return: PIL.Image.Image
        """
        raise "This is an abstract method, don't try to use it."
```

### Implementing a Custom Style

To create a custom style, you need to:

1. Inherit from `AbstractStyle`
2. Call `super().__init__(skin, top_layers, **kwargs)` in your `__init__` method
3. Implement the `image` property to generate the totem texture

Here's a simple example of a custom style that creates a totem with just the head:

```python
from PIL import Image
from wavy_totem_lib.styles.abstract import AbstractStyle
from wavy_totem_lib.options import TopLayer
from wavy_totem_lib.skin import Skin


class HeadOnlyStyle(AbstractStyle):
    def __init__(self, skin: Skin, top_layers: list[TopLayer], **kwargs):
        super().__init__(skin, top_layers, **kwargs)

    @property
    def image(self) -> Image.Image:
        # Add the head to the canvas
        self._canvas.paste(self.skin.head_front, (4, 1))

        # Add the second layer of the head if available and requested
        if self.skin.available_second and TopLayer.HEAD in self.top_layers:
            self._canvas.alpha_composite(self.skin.head_second_front, (4, 1))

        return self._canvas
```

### Using a Custom Style

Once you've created a custom style, you can use it with the `TotemBuilder`:

```python
from wavy_totem_lib import TotemBuilder, Skin
from my_styles import HeadOnlyStyle

builder = TotemBuilder(Skin('my_skin.png'), style=HeadOnlyStyle)
totem = builder.build()
totem.image.save('head_only_totem.png')
```

## Style Implementation Details

When implementing a custom style, you have access to the following:

- `self.skin`: The `Skin` object containing the Minecraft skin
- `self.top_layers`: A list of `TopLayer` enum values indicating which parts should have the second layer applied
- `self.kwargs`: Additional keyword arguments passed to the style constructor
- `self._canvas`: A 16x16 RGBA image that you can draw on to create the totem

The `image` property should return the completed totem image.

## Tips for Creating Custom Styles

- Study the built-in styles (WavyStyle and STTStyle) to understand how they work
- Use the `Skin` class methods to access different parts of the skin
- Check if the second layer is available and requested before applying it
- Remember that the totem image should be 16x16 pixels
- Use `alpha_composite` for transparent overlays
- Consider the differences between slim and wide skins

By creating custom styles, you can customize the appearance of your totems to suit your needs or create unique visual
effects.
