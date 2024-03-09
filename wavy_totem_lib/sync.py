#          Copyright WavyCat 2024 - 2025.
# Distributed under the Boost Software License, Version 1.0.
#        (See accompanying file LICENSE or copy at
#          https://www.boost.org/LICENSE_1_0.txt)

from pathlib import Path
from typing import Union, IO, Optional, Type

from PIL import Image

from .exceptions import EmptyTotem, SmallScale
from .options import SkinType, TopLayers
from .styles.abstract import AbstractStyle
from .styles.wavy import WavyStyle


class TotemBuilder:
    def __init__(self, file: Union[str, bytes, Path, IO[bytes]],
                 style: Type[AbstractStyle] = WavyStyle,
                 skin_type: SkinType = SkinType.AUTO,
                 top_layers: TopLayers = TopLayers.ALL,
                 round_head: bool = False):
        """
        The main class for totem generation.

        Args:
            file: The path or file-like object of the skin image.
            style: A class representing a generation style.
            skin_type: The type of skin to apply to the image.
            top_layers: Determines whether to add an outer layer to the image.
            round_head: Determines whether to round the head shape.

        Example:
            ```
            totem = TotemBuilder('my_skin.png', round_head=True)
            totem.generate()
            totem.scale(10)
            totem.save("totem.png")
            ```
        """

        self._source = Image.open(file)
        self._skin_type = skin_type
        self._top_layers = top_layers
        self._round_head = round_head
        self._style_class = style
        self.raw: Optional[Image.Image] = None

        if self._source.mode != 'RGBA':
            # Convert to RGBA if the mode is not RGBA
            self._source = self._source.convert('RGBA')

        if self._skin_type == SkinType.AUTO:
            # Decide the skin type, if the type is "AUTO"
            self._skin_type = self._detect_skin_type()

    def _detect_skin_type(self) -> SkinType:
        """Detects the skin type based on the transparency of a pixel in the source image."""

        if self._source.height == 32:
            return SkinType.WIDE
        return SkinType.WIDE if bool(self._source.getpixel((46, 52))[3]) else SkinType.SLIM

    def generate(self, **kwargs) -> Image.Image:
        """
        This method generates a totem image using.
        Additional customization can be done by passing keyword arguments (**kwargs) to the method
        (possible options depend on style).
        The generated image will be stored in the `raw` attribute of the object and will also be returned by the method.

        :param kwargs: Additional keyword arguments to customize the created image.
        :return: The generated image.
        """

        totem = self._style_class(self._source, self._skin_type, self._top_layers, **kwargs).image

        if self._round_head:
            # Round the head (if necessary)
            totem.putpixel((4, 1), (0, 0, 0, 0))
            totem.putpixel((11, 1), (0, 0, 0, 0))

        self.raw = totem
        return totem

    def scale(self, factor: int) -> Image.Image:
        """
        Scales the image by the given factor.

        Args:
            factor: The scaling factor.

        Raises:
            EmptyTotem: If the totem has not yet been generated.
            SmallScale: If the scaling factor is less than 1.

        Example:
            ```
            totem = TotemBuilder('my_skin.png')
            totem.generate()
            totem.scale(factor=10) # 16 × 10 = 160px
            ```

        Returns:
            PIL.Image.Image: Generated totem image
        """

        if not self.raw:
            raise EmptyTotem()
        elif factor <= 0:
            raise SmallScale()

        new_image = Image.new('RGBA', (factor * self.raw.width, factor * self.raw.height))

        for x in range(self.raw.width):
            for y in range(self.raw.height):
                colors = self.raw.getpixel((x, y))

                for i in range(factor):
                    for j in range(factor):
                        new_image.putpixel((x * factor + i, y * factor + j), colors)

        self.raw = new_image
        return new_image
