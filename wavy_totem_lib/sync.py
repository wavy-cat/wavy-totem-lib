#          Copyright WavyCat 2024 - 2025.
# Distributed under the Boost Software License, Version 1.0.
#        (See accompanying file LICENSE or copy at
#          https://www.boost.org/LICENSE_1_0.txt)

from pathlib import Path
from typing import Union, IO, Optional

from PIL import Image, ImageOps

from .exceptions import EmptyTotem, SmallScale
from .options import SkinType, TopLayers


class TotemBuilder:
    def __init__(self, file: Union[str, bytes, Path, IO[bytes]],
                 skin_type: SkinType = SkinType.AUTO, top_layers: TopLayers = TopLayers.ALL, round_head: bool = False):
        """
        :param file: The path or file-like object of the skin image.
               Accepted types: str, bytes, Path, IO[bytes]
        :param skin_type: The type of skin to apply to the image.
               Accepted values: SkinType enum object (default: AUTO)
        :param top_layers: Determines whether to add a 2nd layer to the image.
               Accepted values: TopLayers enum object (default: ALL)
        :param round_head: Determines whether to round the head shape.
               Accepted values: bool (default: False)
        """
        self.source = Image.open(file)
        self.skin_type = skin_type
        self.top_layers = top_layers
        self.round_head = round_head
        self.raw: Optional[Image.Image] = None

        if self.source.mode != 'RGBA':
            # Convert to RGBA if the mode is not RGBA
            self.source = self.source.convert('RGBA')

        if self.skin_type == SkinType.AUTO:
            # Decide the skin type, if the type is "AUTO"
            self.skin_type = self._detect_skin_type()

    def _detect_skin_type(self) -> SkinType:
        """
        Detects the skin type based on the transparency of a pixel in the source image.
        """
        if self.source.height == 32:
            return SkinType.WIDE
        return SkinType.WIDE if bool(self.source.getpixel((46, 52))[3]) else SkinType.SLIM

    def _add_hands(self, destination: Image.Image) -> Image.Image:
        """Adding hands to totem image"""
        crop_map = [(((44, 20, 47, 32), (36, 52, 39, 64)), ((44, 20, 48, 32), (36, 52, 40, 64)))]
        dest_left, dest_right = [(3, 8), (2, 8), (1, 8)], [(12, 8), (13, 8), (14, 8)]

        if self.top_layers.value in (1, 6) and self.source.height == 64:
            crop_map.append((((44, 36, 47, 48), (47, 36, 50, 48)), ((44, 36, 48, 48), (48, 36, 52, 48))))

        for m in crop_map:
            if self.skin_type == SkinType.WIDE:
                skin_map = [((0, 0, 4, 1), (3, 1)), ((0, 5, 4, 6), (3, 1)), ((0, 11, 4, 12), (2, 1))]
            else:
                skin_map = [((0, 0, 3, 1), (2, 1)), ((0, 5, 3, 6), (2, 1)), ((0, 11, 3, 12), (2, 1))]

            if self.source.height == 64 and self.skin_type == SkinType.SLIM:
                left_hand, right_hand = self.source.crop(m[0][0]), self.source.crop(m[0][1])
            elif self.source.height == 64 and self.skin_type == SkinType.WIDE:
                left_hand, right_hand = self.source.crop(m[1][0]), self.source.crop(m[1][1])
            else:
                left_hand = right_hand = self.source.crop((44, 20, 48, 32))

            for map_ind, map_val in enumerate(skin_map):
                line_left = left_hand.crop(map_val[0]).resize(map_val[1]).rotate(90, expand=True)
                line_right = right_hand.crop(map_val[0]).resize(map_val[1]).rotate(90, expand=True)

                destination.alpha_composite(line_left, dest_left[map_ind])
                destination.alpha_composite(line_right, dest_right[map_ind])

        return destination

    def _add_legs(self, destination: Image.Image) -> Image.Image:
        """Adds legs to the totem image"""
        if self.source.height == 64:
            legs_right = self.source.crop((20, 52, 24, 64)).crop((0, 11, 4, 12)).resize((2, 1))
            legs_left = self.source.crop((4, 20, 8, 32)).crop((0, 11, 4, 12)).resize((2, 1))
        else:
            legs_left = self.source.crop((5, 21, 8, 32)).resize((2, 1))
            legs_right = ImageOps.flip(legs_left)

        destination.alpha_composite(legs_left, (6, 15))
        destination.alpha_composite(legs_right, (8, 15))

        bottom_region = self.source.crop((22, 31, 26, 32))  # Just above a legs
        destination.alpha_composite(bottom_region, (6, 14))

        return destination

    def _add_torso(self, destination: Image.Image) -> Image.Image:
        """Adds a torso to the totem image"""
        torso = self.source.crop((20, 20, 28, 32)).resize((8, 7))
        destination.paste(torso, (4, 9), torso)

        if self.top_layers.value in (1, 3):
            top_layer_torso = self.source.crop((20, 36, 28, 48)).resize((8, 7))
            destination.alpha_composite(top_layer_torso, (4, 9))

        return destination

    def _add_head(self, destination: Image.Image) -> Image.Image:
        """Adds a head to the totem image"""
        head = self.source.crop((8, 8, 16, 16))
        destination.paste(head, (4, 1))

        if self.top_layers.value in (1, 2, 5, 6):
            top_head_layer = self.source.crop((40, 8, 48, 16))
            destination.alpha_composite(top_head_layer, (4, 1))

        if self.round_head:
            # Round the head (if necessary)
            destination.putpixel((4, 1), (0, 0, 0, 0))
            destination.putpixel((11, 1), (0, 0, 0, 0))

        return destination

    def generate(self) -> Image.Image:
        """
        Generates a ready-made totem image.
        The parameters passed to the __init__ of the class are used.

        :return: The generated image.
        :rtype: Image

        Example usage:
        ```
        totem = TotemBuilder('my_skin.png', SkinType.SLIM, round_head=True)
        totem_image = totem.generate()
        totem_image.show()
        ```
        """

        destination = Image.new("RGBA", (16, 16))

        """Adding body parts"""
        destination = self._add_head(destination)
        destination = self._add_hands(destination)
        destination = self._add_torso(destination)
        destination = self._add_legs(destination)

        """Empty pixels"""
        for i in [(4, 15), (5, 15), (4, 14), (4, 13), (10, 15), (11, 15), (11, 14), (11, 13)]:
            destination.putpixel(i, (0, 0, 0, 0))

        self.raw = destination
        return destination

    def scale(self, factor: int) -> Image.Image:
        """
        Scales the image by the given factor.

        :param factor: The scaling factor.
        :type factor: int
        :raises EmptyTotem: If the totem is not generated.
        :raises SmallScale: If the scaling factor is less than or equal to zero.
        :return: The scaled image.
        :rtype: Image

        Example usage:
        ```
        totem = TotemBuilder('my_skin.png', SkinType.WIDE)
        totem.generate() # Using generate() before scale() is mandatory
        totem_image = totem.scale(factor=16)
        totem_image.show()
        ```
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
