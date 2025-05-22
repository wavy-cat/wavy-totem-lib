#                  Copyright WavyCat 2024.
#  Distributed under the Boost Software License, Version 1.0.
#         (See accompanying file LICENSE or copy at
#           https://www.boost.org/LICENSE_1_0.txt)

from typing import Type

from PIL import Image

from .options import TopLayer
from .exceptions import SmallScale
from .styles.abstract import AbstractStyle


class Totem:
    """
    The `Totem` class represents a Minecraft totem texture.
    Usually this class get after the work of a style or builder.

    :param image: An Image object from PIL.
    :param style: The style used to create the totem.
    :param slim: Determines whether the totem is slim.
    :param top_layers: List of included second layers.
    :param rounded_head: Determines whether the head is rounded or not.
    """
    def __init__(self, image: Image.Image, style: Type[AbstractStyle], slim: bool, top_layers: list[TopLayer],
                 rounded_head: bool):
        self.image = image
        self.slim = slim
        self.style = style
        self.rounded_head = rounded_head
        self.top_layers = top_layers

    def scale(self, *, factor: int) -> Image.Image:
        """
        Scale method scales an image by a given factor.

        :param factor: The factor by which the image will be scaled. Must be greater than 0.
        :rtype factor: int
        :return: The scaled image as an instance of Image from PIL.

        :raises SmallScale: If the scale factor is less than or equal to 0.
        """
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
