#                  Copyright WavyCat 2024.
#  Distributed under the Boost Software License, Version 1.0.
#         (See accompanying file LICENSE or copy at
#           https://www.boost.org/LICENSE_1_0.txt)

from PIL import Image

from .abstract import AbstractStyle
from ..options import TopLayers
from ..skin import Skin


class WavyStyle(AbstractStyle):
    """The default style, which has existed since the first versions. Created by WavyCat."""

    def __init__(self, skin: Skin, top_layers: list[TopLayers], **kwargs):
        super().__init__(skin, top_layers, **kwargs)

    def _add_head(self):
        """Adds a head to the totem image"""
        self._canvas.paste(self.skin.head_front, (4, 1))

        if self.skin.available_second and TopLayers.HEAD in self.top_layers:
            self._canvas.alpha_composite(self.skin.head_second_front, (4, 1))

    def _add_hands(self):
        """Adding hands to totem image"""
        # skin_map is the area of the hand lines and their sizes.
        if self.skin.is_slim:
            skin_map = [((0, 0, 3, 1), (2, 1)), ((0, 5, 3, 6), (2, 1)), ((0, 11, 3, 12), (2, 1))]
        else:
            skin_map = [((0, 0, 4, 1), (3, 1)), ((0, 5, 4, 6), (3, 1)), ((0, 11, 4, 12), (2, 1))]

        # dest_* is the coordinates to insert on the canvas of the totem.
        dest_left, dest_right = [(3, 8), (2, 8), (1, 8)], [(12, 8), (13, 8), (14, 8)]
        left_hand, right_hand = self.skin.left_hand_front, self.skin.right_hand_front
        left_hand_top, right_hand_top = self.skin.left_hand_second_front, self.skin.right_hand_second_front
        use_second_layer = self.skin.available_second and TopLayers.HANDS in self.top_layers

        for map_ind, map_val in enumerate(skin_map):
            line_left = left_hand.crop(map_val[0]).resize(map_val[1]).rotate(90, expand=True)
            line_right = right_hand.crop(map_val[0]).resize(map_val[1]).rotate(90, expand=True)
            self._canvas.paste(line_left, dest_left[map_ind])
            self._canvas.paste(line_right, dest_right[map_ind])

            if use_second_layer:
                line_left = left_hand_top.crop(map_val[0]).resize(map_val[1]).rotate(90, expand=True)
                line_right = right_hand_top.crop(map_val[0]).resize(map_val[1]).rotate(90, expand=True)
                self._canvas.alpha_composite(line_left, dest_left[map_ind])
                self._canvas.alpha_composite(line_right, dest_right[map_ind])

    def _add_torso(self):
        """Adds a torso to the totem image"""
        self._canvas.paste(self.skin.body_front.resize((8, 7)), (4, 9))

        if self.skin.available_second and TopLayers.TORSO in self.top_layers:
            self._canvas.alpha_composite(self.skin.body_second_front.resize((8, 7)), (4, 9))

        # Empty pixels
        for i in [(4, 15), (5, 15), (4, 14), (4, 13), (10, 15), (11, 15), (11, 14), (11, 13)]:
            self._canvas.putpixel(i, (0, 0, 0, 0))

    def _add_legs(self):
        """Adds legs to the totem image"""
        self._canvas.alpha_composite(self.skin.right_leg_front.crop((0, 11, 4, 12)).resize((2, 1)), (6, 15))
        self._canvas.alpha_composite(self.skin.left_leg_front.crop((0, 11, 4, 12)).resize((2, 1)), (8, 15))

        self._canvas.alpha_composite(self.skin.image.crop((22, 31, 26, 32)), (6, 14))  # Just above a legs

        if self.skin.available_second and TopLayers.LEGS in self.top_layers:
            self._canvas.alpha_composite(self.skin.right_leg_second_front.crop((0, 11, 4, 12)).resize((2, 1)), (8, 15))
            self._canvas.alpha_composite(self.skin.left_leg_second_front.crop((0, 11, 4, 12)).resize((2, 1)), (6, 15))

    @property
    def image(self) -> Image.Image:
        """Method that generates a totem image"""
        self._add_head()
        self._add_hands()
        self._add_torso()
        self._add_legs()

        return self._canvas
