#           Copyright WavyCat 2024 - 2025.
#  Distributed under the Boost Software License, Version 1.0.
#         (See accompanying file LICENSE or copy at
#           https://www.boost.org/LICENSE_1_0.txt)

from typing import Type

from PIL import Image

from wavy_totem_lib import SkinType, TopLayers
from wavy_totem_lib.exceptions import SmallScale
from wavy_totem_lib.styles.abstract import AbstractStyle


class Totem:
    def __init__(self, image: Image.Image, model: SkinType, style: Type[AbstractStyle], rounded_head: bool,
                 top_layers: list[TopLayers]):
        self.image = image
        self.model = model
        self.style = style
        self.rounded_head = rounded_head
        self.top_layers = top_layers

    def scale(self, *, factor: int) -> Image.Image:
        if factor <= 0:
            raise SmallScale()

        new_image = Image.new('RGBA', (factor * self.image.width, factor * self.image.height))
        pixels = self.image.load()

        for x in range(self.image.width):
            for y in range(self.image.height):
                for i in range(factor):
                    for j in range(factor):
                        new_image.putpixel((x * factor + i, y * factor + j), pixels[x, y])

        return new_image
