#          Copyright WavyCat 2024 - 2025.
# Distributed under the Boost Software License, Version 1.0.
#        (See accompanying file LICENSE or copy at
#          https://www.boost.org/LICENSE_1_0.txt)

from pathlib import Path
from typing import Union, IO

from PIL import Image

from .exceptions import EmptyTotem, SmallScale
from .options import SkinType


class TotemBuilder:
    def __init__(self, file: Union[str, bytes, Path, IO[bytes]],
                 skin_type: SkinType, use_top_layer: bool = True, round_head: bool = False):
        """
        :param file: The path or file-like object of the image to be processed.
               Accepted types: str, bytes, Path, IO[bytes]
        :param skin_type: The type of skin to apply to the image.
               Accepted values: SkinType enum object
        :param use_top_layer: Determines whether to add a 2nd layer to the image (always active for the head).
               Accepted values: bool (default: True)
        :param round_head: Determines whether to round the head shape.
               Accepted values: bool (default: False)
        """
        self.source = Image.open(file)
        self.skin_type = skin_type
        self.use_top_layer = use_top_layer
        self.round_head = round_head
        self.raw: Image.Image | None = None

        if self.source.mode != 'RGBA':
            # Convert to RGBA if the mode is not RGBA
            self.source = self.source.convert('RGBA')

    def generate(self) -> Image.Image:
        """
        Generates a ready-made totem image. The parameters passed to the __init__ of the class are used.

        :return: The generated image.

        Example usage:
        ```
        totem = TotemBuilder('my_skin.png', SkinType.SLIM, round_head=True)
        totem_image = totem.generate()
        totem_image.show()
        ```
        """

        destination = Image.new("RGBA", (16, 16))

        """Adding a head"""
        head = self.source.crop((8, 8, 16, 16))
        top_head_layer = self.source.crop((40, 8, 48, 16))

        destination.paste(head, (4, 1))
        destination.paste(top_head_layer, (4, 1), top_head_layer)

        if self.round_head:
            # Round the head (if necessary)
            destination.putpixel((4, 1), (0, 0, 0, 0))
            destination.putpixel((11, 1), (0, 0, 0, 0))

        """Adding hands"""
        crop_map = [(((44, 20, 47, 32), (36, 52, 39, 64)), ((44, 20, 48, 32), (36, 52, 40, 64)))]

        if self.use_top_layer:
            crop_map.append((((44, 36, 47, 48), (47, 36, 50, 48)), ((44, 36, 48, 48), (48, 36, 52, 48))))

        for m in crop_map:
            match self.skin_type:
                case SkinType.SLIM:
                    left_hand, right_hand = self.source.crop(m[0][0]), self.source.crop(m[0][1])
                    skin_map = [((0, 0, 3, 1), (2, 1)), ((0, 5, 3, 6), (2, 1)), ((0, 11, 3, 12), (2, 1))]
                case SkinType.WIDE:
                    left_hand, right_hand = self.source.crop(m[1][0]), self.source.crop(m[1][1])
                    skin_map = [((0, 0, 4, 1), (3, 1)), ((0, 5, 4, 6), (3, 1)), ((0, 11, 4, 12), (2, 1))]

            dest_left, dest_right = [(3, 8), (2, 8), (1, 8)], [(12, 8), (13, 8), (14, 8)]

            for map_ind, map_val in enumerate(skin_map):
                line_left = left_hand.crop(map_val[0]).resize(map_val[1]).rotate(90, expand=True)
                line_right = right_hand.crop(map_val[0]).resize(map_val[1]).rotate(90, expand=True)

                destination.alpha_composite(line_left, dest_left[map_ind])
                destination.alpha_composite(line_right, dest_right[map_ind])

        """Adding a torso"""
        torso = self.source.crop((20, 20, 28, 32)).resize((8, 7))
        destination.paste(torso, (4, 9), torso)

        if self.use_top_layer:
            top_layer_torso = self.source.crop((20, 36, 28, 48)).resize((8, 7))
            destination.alpha_composite(top_layer_torso, (4, 9))

        """Bottom part (legs)"""
        legs_right = self.source.crop((20, 52, 24, 64)).crop((0, 11, 4, 12)).resize((2, 1))
        legs_left = self.source.crop((4, 20, 8, 32)).crop((0, 11, 4, 12)).resize((2, 1))

        destination.alpha_composite(legs_left, (6, 15))
        destination.alpha_composite(legs_right, (8, 15))

        bottom_region = self.source.crop((22, 31, 26, 32))  # Just above a legs
        destination.alpha_composite(bottom_region, (6, 14))

        """Empty pixels"""
        for i in [(4, 15), (5, 15), (4, 14), (4, 13), (10, 15), (11, 15), (11, 14), (11, 13)]:
            destination.putpixel(i, (0, 0, 0, 0))

        self.raw = destination
        return destination

    def scale(self, *, factor: int) -> Image.Image:
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
