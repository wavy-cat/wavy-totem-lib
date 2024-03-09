# wavy-totem-lib

![GitHub repo size](https://img.shields.io/github/repo-size/wavy-cat/wavy-totem-lib?style=for-the-badge&logo=github&logoColor=white&labelColor=1A222E&color=242B36&cacheSeconds=0)
![GitHub License](https://img.shields.io/github/license/wavy-cat/wavy-totem-lib?style=for-the-badge&labelColor=1A222E&color=242B36)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/wavy-totem-lib?style=for-the-badge&logo=Python&logoColor=white&label=Version&labelColor=1A222E&color=242B36&cacheSeconds=0)

Python library to generate totems of undying for Minecraft.

## Features

* Support 64x32 skins
* Zoning 2 layers and rounding the head
* Lossless scaling image size
* Asynchrony support
* Built-in CLI [beta]
* Supports PyPy
* Supports different styles

## Requirements

* python >= 3.8
* Pillow >= 10.0.0

## Installing

* Using poetry: `poetry add wavy-totem-lib`
* Using pip: `pip install wavy-totem-lib`

## Using CLI

You can use the library without writing code, from the terminal.
For help, enter the argument `--help` or `-h` (`python3 cli.py --help`).

```
usage: cli.py [-h] [--skin-type [{wide,slim,auto}]]
              [--top-layers [{nothing,all,only_head,only_torso,only_hands,head_and_torso,head_and_hands}]]
              [--round-head [ROUND_HEAD]] [--scale [FACTOR]]
              skin_path totem_path
```

To give an example, the following command opens the skin file **my_skin.png** and creates a totem by **rounding its head**
and saves it to the file **totem.png** at 64×64 resolution (**4x scaling**):

```bash
python3 cli.py my_skin.png totem.png --round-head true --scale 4
```

### Parameters

| Name         | Required? | Valid values                    | Default | Description                                |
|--------------|-----------|---------------------------------|---------|--------------------------------------------|
| skin_path    | ✔         | string                          |         | Path to the skin file                      |
| totem_path   | ✔         | string                          |         | Path where to save the finished totem file |
| --skin-type  | ✖         | string (wide, slim, auto)       | auto    | Indication of what type of skin is used    |
| --top-layers | ✖         | string (see Enum values in CLI) | all     | Indication of zoning 2 layers              |
| --round-head | ✖         | bool                            | false   | Should the head be rounded                 |
| --scale      | ✖         | integer (>0)                    | 1       | Image scaling multiplier                   |

## Examples

* Quick generation:

```python
from wavy_totem_lib import TotemBuilder, TopLayers

totem = TotemBuilder('my_skin.png', top_layers=TopLayers.ONLY_HEAD, round_head=True)
# top_layers=TopLayers.ONLY_HEAD – the outer layer will be applied only to the head
# round_head=True – the head will be rounded at the corners

totem_image = totem.generate()  # Returns a PIL.Image.Image object
totem_image.save('totem.png')
```

* Generation and scaling:

```python
from wavy_totem_lib import TotemBuilder, SkinType

totem = TotemBuilder('my_skin.png', skin_type=SkinType.WIDE)
# skin_type allows you to set the skin type (slim or wide, default auto)

totem.generate()
totem.scale(factor=8) # Scaling from 16×16 to 128×128
totem.raw.show() # Image available in the `raw` variable
```

> [!NOTE]
> To scale up, use the built-in `scale` method instead of `raw.resize` from Pillow, because it may blur the image.

* Asynchronous generation:

```python
import asyncio
from wavy_totem_lib import AsyncTotemBuilder, SkinType, TopLayers

async def main():
    # Using AsyncTotemBuilder class instead of TotemBuilder
    totem = AsyncTotemBuilder('my_skin.png', skin_type=SkinType.SLIM, top_layers=TopLayers.HEAD_AND_HANDS)
    await totem.generate()
    await totem.scale(factor=4) # 64×64
    await totem.save('totem.png') # save() is only available in AsyncTotemBuilder

asyncio.run(main())
```

> [!NOTE]
> Although the methods `generate()`, `scale()` and the variable `raw` return values of type `PIL.Image.Image`, suitable for saving a file, it's advisable to use the built-in asynchronous save method instead.

* Specifying a style

```python
from wavy_totem_lib import TotemBuilder, STTStyle

# WavyStyle (default), STTStyle available
totem = TotemBuilder('my_skin.png', style=STTStyle)
totem.generate()
totem.raw.save('totem.png')
```

> [!NOTE]
> The `generate()` method accepts **kwargs, which will be passed on to the style class. None of the built-in styles support them.

> STTStyle taken from https://github.com/UnFamousSoul/STT

## Enum values

**SkinType**: `WIDE`, `SLIM`, `AUTO`

**TopLayers**: `NOTHING`, `ALL`, `ONLY_HEAD`, `ONLY_TORSO`, `ONLY_HANDS`, `HEAD_AND_TORSO`, `HEAD_AND_HANDS`

### In CLI

**skin-type**: `wide`, `slim`, `auto`

**top-layers**: `nothing`, `all`, `only_head`, `only_torso`, `only_hands`, `head_and_torso`, `head_and_hands`
