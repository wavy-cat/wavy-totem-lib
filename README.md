# wavy-totem-lib
![GitHub repo size](https://img.shields.io/github/repo-size/wavy-cat/wavy-totem-lib?style=for-the-badge&logo=github&logoColor=white&labelColor=1A222E&color=242B36&cacheSeconds=0)

Python library to generate totems of undying for Minecraft

## Features

* Support 64x32 skins
* Zoning 2 layers
* Lossless scaling image size

## Requirements
* python >= 3.10
* Pillow >= 10.2.0

## Installing

Clone the repository, or [download](https://github.com/wavy-cat/wavy-totem-lib/archive/refs/heads/main.zip) and extract the files from the project's ZIP archive.
After this, install the library in your environment:

* Using poetry: `poetry add /path/to/wavy-totem-lib`
* Using pip: `pip install /path/to/wavy-totem-lib`

## Using CLI

You can use the library without writing code from the terminal.
For help, enter the argument `--help` or `-h`:

```bash
python3 cli.py --help
```

To give an example, the following command opens the skin file **my-skin.png** and creates a totem by **rounding its head** and saves it to the file **totem.png** at 64×64 resolution (**4x scaling**):

```bash
python3 cli.py my-skin.png totem.png --round-head true --scale 4
```

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
totem.raw.show()  # PIL.Image is available in the `raw` variable
```

> [!IMPORTANT]
> To scale up, use the built-in `scale` method instead of `raw.resize` from Pillow, because it may blur the image.

## Enum values

**SkinType**: `WIDE`, `SLIM`, `AUTO`

**TopLayers**: `NOTHING`, `ALL`, `ONLY_HEAD`, `ONLY_TORSO`, `ONLY_HANDS`, `HEAD_AND_TORSO`, `HEAD_AND_HANDS`
