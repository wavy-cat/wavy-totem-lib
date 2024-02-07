#          Copyright WavyCat 2024 - 2025.
# Distributed under the Boost Software License, Version 1.0.
#    (See accompanying file LICENSE_1_0.txt or copy at
#          https://www.boost.org/LICENSE_1_0.txt)

from pathlib import Path
from typing import Union, IO

from PIL import Image

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
        match self.skin_type:
            case SkinType.SLIM:
                left_hand, right_hand = self.source.crop((44, 20, 47, 32)), self.source.crop((36, 52, 39, 64))
                skin_map = [((0, 0, 3, 1), (2, 1)), ((0, 5, 3, 6), (2, 1)), ((0, 11, 3, 12), (2, 1))]
            case SkinType.WIDE:
                left_hand, right_hand = self.source.crop((44, 20, 48, 32)), self.source.crop((36, 52, 40, 64))
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

        """Adding second layers"""
        if self.use_top_layer:
            """Hands"""
            match self.skin_type:
                case SkinType.SLIM:
                    left_hand, right_hand = self.source.crop((44, 36, 47, 48)), self.source.crop((47, 36, 50, 48))
                    skin_map = [((0, 0, 3, 1), (2, 1)), ((0, 5, 3, 6), (2, 1)), ((0, 11, 3, 12), (2, 1))]
                case SkinType.WIDE:
                    left_hand, right_hand = self.source.crop((44, 36, 48, 48)), self.source.crop((48, 36, 52, 48))
                    skin_map = [((0, 0, 4, 1), (3, 1)), ((0, 5, 4, 6), (3, 1)), ((0, 11, 4, 12), (2, 1))]

            for map_ind, map_val in enumerate(skin_map):
                line_left = left_hand.crop(map_val[0]).resize(map_val[1]).rotate(90, expand=True)
                line_right = right_hand.crop(map_val[0]).resize(map_val[1]).rotate(90, expand=True)

                destination.alpha_composite(line_left, dest_left[map_ind])
                destination.alpha_composite(line_right, dest_right[map_ind])

            """Torso"""
            top_layer_torso = self.source.crop((20, 36, 28, 48)).resize((8, 7))
            destination.alpha_composite(top_layer_torso, (4, 9))

        """Bottom part (legs)"""
        legs_right = self.source.crop((20, 52, 24, 64)).crop((0, 11, 4, 12)).resize((2, 1))
        legs_left = self.source.crop((4, 20, 8, 32)).crop((0, 11, 4, 12)).resize((2, 1))

        destination.paste(legs_left, (6, 15), legs_left)
        destination.paste(legs_right, (8, 15), legs_right)

        bottom_region = self.source.crop((22, 31, 26, 32))  # Just above a legs
        destination.paste(bottom_region, (6, 14), bottom_region)

        """Empty pixels"""
        for i in [(4, 15), (5, 15), (4, 14), (4, 13), (10, 15), (11, 15), (11, 14), (11, 13)]:
            destination.putpixel(i, (0, 0, 0, 0))

        return destination
