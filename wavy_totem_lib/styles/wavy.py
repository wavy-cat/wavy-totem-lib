#          Copyright WavyCat 2024 - 2025.
# Distributed under the Boost Software License, Version 1.0.
#        (See accompanying file LICENSE or copy at
#          https://www.boost.org/LICENSE_1_0.txt)

from PIL import Image, ImageOps

from .abstract import AbstractStyle
from ..options import SkinType, TopLayers


class WavyStyle(AbstractStyle):
    """The default style, which has existed since the first versions. Created by WavyCat."""

    def __init__(self, skin: Image.Image, skin_type: SkinType, top_layers: TopLayers, **kwargs):
        super().__init__(skin, skin_type, top_layers, **kwargs)

    def _add_hands(self):
        """Adding hands to totem image"""
        crop_map = [(((44, 20, 47, 32), (36, 52, 39, 64)), ((44, 20, 48, 32), (36, 52, 40, 64)))]
        dest_left, dest_right = [(3, 8), (2, 8), (1, 8)], [(12, 8), (13, 8), (14, 8)]

        if self._top_layers.value in (1, 6) and self._source.height == 64:
            crop_map.append((((44, 36, 47, 48), (47, 36, 50, 48)), ((44, 36, 48, 48), (48, 36, 52, 48))))

        for m in crop_map:
            if self._skin_type == SkinType.WIDE:
                skin_map = [((0, 0, 4, 1), (3, 1)), ((0, 5, 4, 6), (3, 1)), ((0, 11, 4, 12), (2, 1))]
            else:
                skin_map = [((0, 0, 3, 1), (2, 1)), ((0, 5, 3, 6), (2, 1)), ((0, 11, 3, 12), (2, 1))]

            if self._source.height == 64 and self._skin_type == SkinType.SLIM:
                left_hand, right_hand = self._source.crop(m[0][0]), self._source.crop(m[0][1])
            elif self._source.height == 64 and self._skin_type == SkinType.WIDE:
                left_hand, right_hand = self._source.crop(m[1][0]), self._source.crop(m[1][1])
            else:
                left_hand = right_hand = self._source.crop((44, 20, 48, 32))

            for map_ind, map_val in enumerate(skin_map):
                line_left = left_hand.crop(map_val[0]).resize(map_val[1]).rotate(90, expand=True)
                line_right = right_hand.crop(map_val[0]).resize(map_val[1]).rotate(90, expand=True)

                self._canvas.alpha_composite(line_left, dest_left[map_ind])
                self._canvas.alpha_composite(line_right, dest_right[map_ind])

    def _add_legs(self):
        """Adds legs to the totem image"""
        if self._source.height == 64:
            legs_right = self._source.crop((20, 52, 24, 64)).crop((0, 11, 4, 12)).resize((2, 1))
            legs_left = self._source.crop((4, 20, 8, 32)).crop((0, 11, 4, 12)).resize((2, 1))
        else:
            legs_left = self._source.crop((5, 21, 8, 32)).resize((2, 1))
            legs_right = ImageOps.flip(legs_left)

        self._canvas.alpha_composite(legs_left, (6, 15))
        self._canvas.alpha_composite(legs_right, (8, 15))

        bottom_region = self._source.crop((22, 31, 26, 32))  # Just above a legs
        self._canvas.alpha_composite(bottom_region, (6, 14))

    def _add_torso(self):
        """Adds a torso to the totem image"""
        torso = self._source.crop((20, 20, 28, 32)).resize((8, 7))
        self._canvas.paste(torso, (4, 9), torso)

        if self._top_layers.value in (1, 3):
            top_layer_torso = self._source.crop((20, 36, 28, 48)).resize((8, 7))
            self._canvas.alpha_composite(top_layer_torso, (4, 9))

    def _add_head(self):
        """Adds a head to the totem image"""
        head = self._source.crop((8, 8, 16, 16))
        self._canvas.paste(head, (4, 1))

        if self._top_layers.value in (1, 2, 5, 6):
            top_head_layer = self._source.crop((40, 8, 48, 16))
            self._canvas.alpha_composite(top_head_layer, (4, 1))

    @property
    def image(self) -> Image.Image:
        """Method that generates a totem image"""
        self._add_head()
        self._add_hands()
        self._add_torso()
        self._add_legs()

        """Empty pixels"""
        for i in [(4, 15), (5, 15), (4, 14), (4, 13), (10, 15), (11, 15), (11, 14), (11, 13)]:
            self._canvas.putpixel(i, (0, 0, 0, 0))

        return self._canvas
