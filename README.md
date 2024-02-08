# wavy-totem-lib
Python library to generate totems of undying for Minecraft

## Requirements
* python >= 3.10
* Pillow >= 10.2.0

## Installing

Clone the repository, or download and extract the ZIP archive of the project.
After this, install the library in your environment:

* Using poetry: `poetry add /path/to/wavy-totem-lib`
* Using pip: `pip install /path/to/wavy-totem-lib`

## Examples

Quick generation:

```python
from wavy_totem_lib import TotemBuilder, SkinType

totem = TotemBuilder('my_skin.png', SkinType.SLIM, round_head=True, use_top_layer=False)
totem_image = totem.generate()
totem_image.save('totem.png')
```

Generation and scaling:

```python
from wavy_totem_lib import TotemBuilder, SkinType

totem = TotemBuilder('my_skin.png', SkinType.WIDE)
totem.generate()
totem.scale(8)  # Scaling from 16×16 to 128×128
totem.raw.save('totem.png')  # The totem image is available in the raw variable
```

> [!NOTE]
> To scale an image up, use the built-in `.scale()` instead of Pillow's `raw.resize()` because it can blur the image.
