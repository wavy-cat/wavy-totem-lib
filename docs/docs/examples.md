---
sidebar_position: 3
---

# Examples

This section provides various examples of how to use TotemLib for different scenarios.

## Generation and Scaling

One of the key features of TotemLib is the ability to scale the generated totem without losing quality. Here's how to generate a totem and scale it:

```python
from wavy_totem_lib import TotemBuilder, Skin, Totem

# Create a builder with a slim skin
builder = TotemBuilder(Skin('my_skin.png', slim=True))

# Build the totem
totem: Totem = builder.build()

# Scale the totem from 16×16 to 128×128
scaled = totem.scale(factor=8)

# Save the scaled totem
scaled.save('totem.png')
```

> **Note**: To scale up, use the built-in `scale()` method instead of `resize()` from Pillow, because the latter may blur the image. The `scale()` method performs pixel-perfect scaling that preserves the pixelated look of Minecraft textures.

## Asynchronous Generation

For applications that need to generate multiple totems or avoid blocking the main thread, wavy-totem-lib provides asynchronous support:

```python
import asyncio
from io import BytesIO
from wavy_totem_lib import TotemBuilder, Skin, Totem, TopLayer
# To save a file asynchronously, install the aiofiles package
import aiofiles


async def main():
    builder = TotemBuilder(Skin('my_skin.png', slim=False),
                           top_layers=[TopLayer.HEAD, TopLayer.HANDS],
                           round_head=True)
    
    # Build the totem asynchronously
    totem: Totem = await builder.build_async()
    
    # Save the totem to a BytesIO object
    temp = BytesIO()
    totem.image.save(temp, format='png')

    # Save the totem to a file asynchronously
    async with aiofiles.open('totem.png', 'wb') as f:
        await f.write(temp.getvalue())


asyncio.run(main())
```

## Using Different Styles

wavy-totem-lib comes with two built-in styles: WavyStyle (default) and STTStyle. Here's how to use the STTStyle:

```python
from wavy_totem_lib import TotemBuilder, Skin, Totem, STTStyle

# Create a builder with the STTStyle
builder = TotemBuilder(Skin('my_skin.png'), style=STTStyle)

# Build the totem
totem: Totem = builder.build()

# Save the totem
totem.image.save('totem.png')
```

## Customizing Top Layers

You can specify which parts of the skin should use the second layer (overlay):

```python
from wavy_totem_lib import TotemBuilder, Skin, TopLayer

# Apply the second layer only to the head and hands
builder = TotemBuilder(
    Skin('my_skin.png'),
    top_layers=[TopLayer.HEAD, TopLayer.HANDS]
)

# Build and save the totem
totem = builder.build()
totem.image.save('totem.png')
```

The available top layers are:
- `TopLayer.HEAD`: Apply the second layer to the head
- `TopLayer.TORSO`: Apply the second layer to the torso
- `TopLayer.HANDS`: Apply the second layer to the hands
- `TopLayer.LEGS`: Apply the second layer to the legs

You can also use `ALL_TOP_LAYERS` to apply the second layer to all parts (this is the default).
