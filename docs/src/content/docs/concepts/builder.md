---
title: Builder
description: Learn about the concept of the Totem Builder
---

The Builder (also known as TotemBuilder) is a helper class that wraps all library components and provides a convenient `build()` method for generating the totem.

## Usage

```py
from wavy_totem_lib import TotemBuilder, Skin, TopLayer
from wavy_totem_lib.patterns import STT

builder = TotemBuilder(
    skin=Skin('my_skin.png', slim=True),
    pattern=STT,  # Specifying the pattern
    top_layers=[TopLayer.HEAD, TopLayer.HANDS],  # Specifying body parts for which to render the top layer
    round_head=True  # Specifying whether to round the head
)

# Generating the totem
totem = builder.build()
```

The Builder accepts several arguments:

* `skin`: `Skin` - your [skin](/concepts/skin/) object. This is the only required argument;
* `pattern`: `Type[Abstract]` (default: [Wavy](/concepts/pattern#wavy)) - the required [pattern](/concepts/pattern) to be used for totem generation;
* `top_layers`: `list[TopLayer] | None` (default: ALL_TOP_LAYERS) - a list of body parts of the TopLayer enum type for which the top layer should be rendered. If the top layer is not needed, pass an empty list or None. This list is passed to the pattern; the Builder itself does not process it.
* `round_head`: `bool` (default: False) - specifies whether to "round" the head, i.e., remove the 2 top pixels at the edges of the head. This functionality is implemented by the Builder itself. Visual example:

| Without Rounding                                                                        | With Rounding                                                                      |
|----------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| ![Notch. Head rounding example.](../../../assets/examples/builder/no-rounded.webp) | ![Notch. Head rounding example.](../../../assets/examples/builder/rounded.webp) |

The Builder returns an instance of the [Totem](/concepts/totem) class.

### Asynchronous Usage

In asynchronous code, you can use the `build_async()` method instead of the synchronous `build()`.
Essentially, this method is an asynchronous wrapper around `build()`.

```py
from wavy_totem_lib import TotemBuilder, Skin, TopLayer
from wavy_totem_lib.patterns import STT


async def build_totem():
    builder = TotemBuilder(
        skin=Skin('my_skin.png', slim=True),
        pattern=STT,
        top_layers=[TopLayer.HEAD, TopLayer.HANDS],
        round_head=True
    )

    # Asynchronous totem generation
    totem = await builder.build_async()
```