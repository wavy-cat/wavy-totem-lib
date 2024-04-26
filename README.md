# wavy-totem-lib

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/wavy-totem-lib?style=for-the-badge&logo=Python&logoColor=white&label=Version&labelColor=1A222E&color=242B36&cacheSeconds=0)
![GitHub License](https://img.shields.io/github/license/wavy-cat/wavy-totem-lib?style=for-the-badge&labelColor=1A222E&color=242B36)
![GitHub repo size](https://img.shields.io/github/repo-size/wavy-cat/wavy-totem-lib?style=for-the-badge&logo=github&logoColor=white&labelColor=1A222E&color=242B36&cacheSeconds=0)

Python library to generate totems of undying for Minecraft.

## Features

* Support 64x32 skins
* Zoning 2 layers and rounding the head
* Lossless scaling image size
* Asynchrony support
* Supports PyPy
* Supports different styles

## Requirements

* python >= 3.8
* Pillow >= 10.0.0

## Installing

* Using poetry: `poetry add wavy-totem-lib`
* Using pip: `pip install wavy-totem-lib`

## Examples

* Quick generation:

```python
from wavy_totem_lib import TotemBuilder, Skin, Totem, TopLayers

builder = TotemBuilder(
    Skin('my_skin.png'),
    top_layers=[TopLayers.HEAD],  # the second layer will be applied only to the head
    round_head=True  # the head will be rounded at the corners
)

totem: Totem = builder.build()
totem.image.save('totem.png')  # .image is Pillow image
```

* Generation and scaling:

```python
from wavy_totem_lib import TotemBuilder, Skin, Totem, TopLayers

builder = TotemBuilder(Skin('my_skin.png', slim=True))

totem: Totem = builder.build()
scaled = totem.scale(factor=8)  # Scaling from 16×16 to 128×128
scaled.save('totem.png')
```

> [!NOTE]
> To scale up, use the built-in `scale` method instead of `raw.resize` from Pillow, because it may blur the image.

* Asynchronous generation:

```python
import asyncio
import aiofiles  # This package must be installed
from io import BytesIO
from wavy_totem_lib import TotemBuilder, Skin, Totem, TopLayers


async def main():
    builder = TotemBuilder(Skin('my_skin.png', slim=False),
                           top_layers=[TopLayers.HEAD, TopLayers.HANDS],
                           round_head=True)
    totem: Totem = await builder.build_async()
    temp = BytesIO()
    totem.image.save(temp, format='png')

    async with aiofiles.open('totem.png', 'wb') as f:
        await f.write(temp.getvalue())


asyncio.run(main())
```

* Specifying a style

```python
from wavy_totem_lib import TotemBuilder, Skin, Totem, STTStyle

# WavyStyle (default), STTStyle available built-in
builder = TotemBuilder(Skin('my_skin.png'), style=STTStyle)
totem: Totem = builder.build()
totem.image.save('totem.png')
```

> [!NOTE]
> The `generate()` method accepts **kwargs, which will be passed on to the style class. None of the built-in styles
> support them.

> STTStyle taken from https://github.com/UnFamousSoul/STT

## Styles

> [!IMPORTANT]
> You can create your own styles by inheriting the `AbstractStyle` class and implementing the `image` property.

### Wavy

Created by @wavy-cat.
Class name: `WavyStyle`.
This is the default style in TotemBuilder.

| Basil                           | Sylphiette                           | PWGood                           |
|---------------------------------|--------------------------------------|----------------------------------|
| ![Image](assets/basil_wavy.png) | ![Image](assets/sylphiette_wavy.png) | ![Image](assets/pwgood_wavy.png) |

```python
from wavy_totem_lib import TotemBuilder, WavyStyle

TotemBuilder(style=WavyStyle)
# You can also not specify style at all, because WavyStyle - default style
```

### STT

Created by @UnFamousSoul.
The code is taken from the [UnFamousSoul/STT](https://github.com/UnFamousSoul/STT) repository.
Class name: `STTStyle`.

| Basil                          | Sylphiette                          | PWGood                          |
|--------------------------------|-------------------------------------|---------------------------------|
| ![Image](assets/basil_stt.png) | ![Image](assets/sylphiette_stt.png) | ![Image](assets/pwgood_stt.png) |

```python
from wavy_totem_lib import TotemBuilder, STTStyle

TotemBuilder(style=STTStyle)
```