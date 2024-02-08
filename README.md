# wavy-totem-lib
Python library to generate totems of undying for Minecraft

## Features

* Support 64x32 skins
* Zoning 2 layers
* Lossless scaling image size

## Requirements
* python >= 3.10
* Pillow >= 10.2.0

## Installing

Clone the repository, or [download](https://github.com/wavy-cat/wavy-totem-lib/archive/refs/heads/main.zip) and extract the ZIP archive of the project.
After this, install the library in your environment:

* Using poetry: `poetry add /path/to/wavy-totem-lib`
* Using pip: `pip install /path/to/wavy-totem-lib`

## Examples

Quick generation:

```python
from wavy_totem_lib import TotemBuilder, SkinType, TopLayers

totem = TotemBuilder('my_skin.png', SkinType.AUTO, top_layers=TopLayers.ALL, round_head=True)
totem_image = totem.generate()
totem_image.save('totem.png')
```

Generation and scaling:

```python
from wavy_totem_lib import TotemBuilder, SkinType

totem = TotemBuilder('my_skin.png', SkinType.WIDE)
totem.generate()
totem.scale(factor=8)  # Scaling from 16×16 to 128×128
totem.raw.save('totem.png')  # PIL.Image is available in the `raw` variable
```

> [!IMPORTANT]
> To scale an image up, use the built-in `.scale()` instead of Pillow's `raw.resize()` because it can blur the image.

## Enum values

**SkinType**: `WIDE`, `SLIM`, `AUTO`

**TopLayers**: `NOTHING`, `ALL`, `ONLY_HEAD`, `ONLY_TORSO`, `ONLY_HANDS`, `HEAD_AND_TORSO`, `HEAD_AND_HANDS`
