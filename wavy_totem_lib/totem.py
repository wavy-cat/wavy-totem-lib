from typing import Type

from PIL import Image

from .layers import TopLayer
from .exceptions import SmallScale
from .patterns.abstract import Abstract


class Totem:
    """
    The `Totem` class represents a Minecraft totem texture.
    Usually this class get after the work of a style or builder.

    :param image: An Image object from PIL.
    :param pattern: The pattern used to create the totem.
    :param slim: Determines whether the totem is slim.
    :param top_layers: List of included second layers.
    :param rounded_head: Determines whether the head is rounded or not.
    """
    def __init__(self, image: Image.Image, pattern: Type[Abstract], slim: bool, top_layers: list[TopLayer],
                 rounded_head: bool):
        self.image = image
        self.slim = slim
        self.pattern = pattern
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
