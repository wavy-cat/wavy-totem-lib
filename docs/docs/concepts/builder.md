---
sidebar_position: 3
---

# TotemBuilder

The `TotemBuilder` class is a key component of wavy-totem-lib that simplifies the process of creating totems from Minecraft skins.

## Overview

The `TotemBuilder` class follows the builder pattern, providing a convenient way to configure and create a `Totem` object. It handles the application of styles to a skin and manages various options like top layers and head rounding.

## Creating a TotemBuilder

To create a `TotemBuilder`, you need to provide a `Skin` object and optionally specify a style, top layers, and whether to round the head:

```python
from wavy_totem_lib import TotemBuilder, Skin, WavyStyle, TopLayer

# Basic builder with default options
builder = TotemBuilder(Skin('my_skin.png'))

# Builder with custom options
custom_builder = TotemBuilder(
    skin=Skin('my_skin.png', slim=True),
    style=WavyStyle,  # This is the default style
    top_layers=[TopLayer.HEAD, TopLayer.HANDS],  # Only apply second layer to head and hands
    round_head=True  # Round the corners of the head
)
```

## Constructor Parameters

The `TotemBuilder` constructor accepts the following parameters:

- `skin` (required): A `Skin` object representing the Minecraft skin to use
- `style` (optional): The style class to use for building the totem (defaults to `WavyStyle`)
- `top_layers` (optional): A list of `TopLayer` enum values indicating which parts should have the second layer applied (defaults to all layers)
- `round_head` (optional): A boolean indicating whether to round the corners of the head (defaults to `False`)

## Building a Totem

Once you've created a `TotemBuilder`, you can build a totem using one of two methods:

### Synchronous Building

The `build` method builds a totem synchronously:

```python
from wavy_totem_lib import TotemBuilder, Skin

builder = TotemBuilder(Skin('my_skin.png'))
totem = builder.build()
```

The `build` method also accepts additional keyword arguments that will be passed to the style's constructor:

```python
# Pass additional arguments to the style
totem = builder.build(custom_option=True)
```

Note that the built-in styles (WavyStyle and STTStyle) don't accept any additional arguments.

### Asynchronous Building

The `build_async` method builds a totem asynchronously, which is useful for applications that need to avoid blocking the main thread:

```python
import asyncio
from wavy_totem_lib import TotemBuilder, Skin

async def generate_totem():
    builder = TotemBuilder(Skin('my_skin.png'))
    totem = await builder.build_async()
    return totem

# Run the async function
totem = asyncio.run(generate_totem())
```

The `build_async` method accepts the following parameters:

- `loop` (optional): An event loop to use for the asynchronous operation (defaults to the current event loop)
- `executor` (optional): An executor to use for running the build method (defaults to `ThreadPoolExecutor`)
- Additional keyword arguments that will be passed to the style's constructor

## Top Layers

The `top_layers` parameter allows you to specify which parts of the skin should have the second layer (overlay) applied. This is useful for customizing the appearance of the totem.

The available top layers are defined in the `TopLayer` enum:

- `TopLayer.HEAD`: Apply the second layer to the head
- `TopLayer.TORSO`: Apply the second layer to the torso
- `TopLayer.HANDS`: Apply the second layer to the hands
- `TopLayer.LEGS`: Apply the second layer to the legs

You can also use `ALL_TOP_LAYERS` to apply the second layer to all parts (this is the default):

```python
from wavy_totem_lib import TotemBuilder, Skin, TopLayer, ALL_TOP_LAYERS

# Apply second layer to all parts (default)
builder1 = TotemBuilder(Skin('my_skin.png'), top_layers=ALL_TOP_LAYERS)

# Apply second layer only to head and hands
builder2 = TotemBuilder(Skin('my_skin.png'), top_layers=[TopLayer.HEAD, TopLayer.HANDS])

# Don't apply second layer to any part
builder3 = TotemBuilder(Skin('my_skin.png'), top_layers=[])
```

## Rounding the Head

The `round_head` parameter allows you to round the corners of the head, which can give the totem a more polished look:

```python
from wavy_totem_lib import TotemBuilder, Skin

# Create a builder with rounded head
builder = TotemBuilder(Skin('my_skin.png'), round_head=True)
```

When `round_head` is set to `True`, the builder will make the top corners of the head transparent, creating a rounded appearance.

## Complete Example

Here's a complete example that demonstrates the various features of the `TotemBuilder` class:

```python
from wavy_totem_lib import TotemBuilder, Skin, TopLayer, STTStyle

# Create a builder with custom options
builder = TotemBuilder(
    skin=Skin('my_skin.png'),
    style=STTStyle,
    top_layers=[TopLayer.HEAD, TopLayer.HANDS],
    round_head=True
)

# Build the totem
totem = builder.build()

# Scale and save the totem
totem.scale(factor=8).save('my_totem.png')
```

This example creates a totem using the STTStyle, applies the second layer only to the head and hands, rounds the head, scales the result by a factor of 8, and saves it to a file.