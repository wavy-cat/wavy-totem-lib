# TotemLib (aka wavy-totem-lib)

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

<p align="center">
  <img src=".github/assets/notch_stt.png" width="20%">
  <img src=".github/assets/wavycat_wavy.png" width="20%">
  <img src=".github/assets/cyceku_wavy.png" width="20%">
</p>

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
