# TotemLib

aka **wavy-totem-lib**

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/wavy-totem-lib?style=for-the-badge&logo=Python&logoColor=white&label=Version&labelColor=1A222E&color=242B36&cacheSeconds=0)
![GitHub License](https://img.shields.io/github/license/wavy-cat/wavy-totem-lib?style=for-the-badge&labelColor=1A222E&color=242B36)
![GitHub repo size](https://img.shields.io/github/repo-size/wavy-cat/wavy-totem-lib?style=for-the-badge&logo=github&logoColor=white&labelColor=1A222E&color=242B36&cacheSeconds=0)

Python library to generate totems of undying for Minecraft.

---

## Features

* Support 64x32 skins
* Zoning 2 layers and rounding the head
* Lossless scaling image size
* Asynchrony support
* Supports PyPy
* Supports different patterns (styles)

## Documentation

The documentation is available at https://totemlib.wavycat.me, as well as https://totemlib-docs.wavycat.workers.dev.

## Installing

#### Using uv

```bash
uv add wavy-totem-lib
```

#### Using Poetry

```bash
poetry add wavy-totem-lib
```

#### Using pip

```bash
pip install wavy-totem-lib
```

## Quick start

```python
from wavy_totem_lib import TotemBuilder, Skin, Totem, TopLayer

builder = TotemBuilder(
    Skin('my_skin.png'),
    top_layers=[TopLayer.HEAD],  # the second layer will be applied only to the head
    round_head=True  # the head will be rounded at the corners
)

totem: Totem = builder.build()
totem.image.save('totem.png')  # .image is Pillow image
```

### More examples

<details>
<summary>Generation and scaling</summary>

```python
from wavy_totem_lib import TotemBuilder, Skin, Totem

builder = TotemBuilder(Skin('my_skin.png', slim=True))

totem: Totem = builder.build()
scaled = totem.scale(factor=8)  # Scaling from 16×16 to 128×128
scaled.save('totem.png')
```

> To scale up, use the built-in `scale()` method instead of `resize()` from Pillow, because it may blur the image.

</details>

<details>
<summary>Asynchronous generation</summary>

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
    totem: Totem = await builder.build_async()
    temp = BytesIO()
    totem.image.save(temp, format='png')

    async with aiofiles.open('totem.png', 'wb') as f:
        await f.write(temp.getvalue())


asyncio.run(main())
```

</details>

<details>
<summary>Specifying a pattern</summary>

```python
from wavy_totem_lib import TotemBuilder, Skin, Totem
from wavy_totem_lib.patterns import STT

# Wavy is default, STT available built-in
builder = TotemBuilder(Skin('my_skin.png'), pattern=STT)
totem: Totem = builder.build()
totem.image.save('totem.png')
```

> The `generate()` method accepts **kwargs, which will be passed on to the pattern class. None of the built-in patterns
> support them.

</details>

## Patterns

> [!NOTE]
> You can create your own pattern by creating subclass from `Abstract` class and implementing the `image` method.

### Wavy

This is the default pattern in TotemBuilder.

| [Notch](https://namemc.com/profile/Notch.1) (wide) | [WavyCat](https://namemc.com/profile/_WavyCat_.1) (slim) | [CyCeKu](https://namemc.com/profile/CyCeKu.1) (wide) |
|----------------------------------------------------|----------------------------------------------------------|------------------------------------------------------|
| ![Skin](.github/assets/notch_wavy.png)             | ![Skin](.github/assets/wavycat_wavy.png)                 | ![Skin](.github/assets/cyceku_wavy.png)              |

```python
from wavy_totem_lib import TotemBuilder
from wavy_totem_lib.patterns import Wavy

TotemBuilder(pattern=Wavy)
# You can also not specify the pattern at all, because WavyStyle – default pattern.
```

### STT

The code is taken from the [UnFamousSoul/STT](https://github.com/UnFamousSoul/STT) repository.

| [Notch](https://namemc.com/profile/Notch.1) (wide) | [WavyCat](https://namemc.com/profile/_WavyCat_.1) (slim) | [CyCeKu](https://namemc.com/profile/CyCeKu.1) (wide) |
|----------------------------------------------------|----------------------------------------------------------|------------------------------------------------------|
| ![Skin](.github/assets/notch_stt.png)              | ![Skin](.github/assets/wavycat_stt.png)                  | ![Skin](.github/assets/cyceku_stt.png)               |

```python
from wavy_totem_lib import TotemBuilder
from wavy_totem_lib.patterns import STT

TotemBuilder(pattern=STT)
```
