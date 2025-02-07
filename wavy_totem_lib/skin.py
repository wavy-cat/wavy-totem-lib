#                  Copyright WavyCat 2024.
#  Distributed under the Boost Software License, Version 1.0.
#         (See accompanying file LICENSE or copy at
#           https://www.boost.org/LICENSE_1_0.txt)

from pathlib import Path
from typing import Union, IO, Optional, Dict

from PIL import Image


class Skin:
    def __init__(self, filepath: Union[str, bytes, Path, IO[bytes]], slim: bool = ...):
        self.image = Image.open(filepath)

        if self.image.mode != 'RGBA':
            # Convert to RGBA if the mode differs from RGBA
            self.image = self.image.convert('RGBA')

        self.version = 'new' if self.image.height == 64 else 'old'
        self.available_second = True if self.version == 'new' else False
        self.is_slim = self._detect_slim() if slim is ... else slim

    def _detect_slim(self) -> bool:
        """
        Detects the skin type based on the transparency of a pixel in the source image.
        False – wide, True – slim.
        """

        if self.image.height == 32:
            return False
        return False if bool(self.image.getpixel((46, 52))[3]) else True

    @property
    def right_leg(self) -> Dict[str, Image.Image]:
        # Note on side placement on skins
        # Top, Bottom
        # Left, Front, Right, Back.
        return {
            'front': self.image.crop((4, 20, 8, 32)),
            'back': self.image.crop((12, 20, 16, 32)),
            'left': self.image.crop((0, 20, 4, 32)),
            'right': self.image.crop((8, 20, 12, 32)),
            'top': self.image.crop((4, 16, 8, 20)),
            'bottom': self.image.crop((8, 16, 12, 20))
        }

    @property
    def right_leg_front(self) -> Image.Image:
        return self.image.crop((4, 20, 8, 32))

    @property
    def right_leg_second(self) -> Optional[Dict[str, Image.Image]]:
        if not self.available_second:
            return None

        return {
            'front': self.image.crop((4, 36, 8, 48)),
            'back': self.image.crop((12, 36, 16, 48)),
            'left': self.image.crop((0, 36, 4, 48)),
            'right': self.image.crop((8, 36, 12, 48)),
            'top': self.image.crop((4, 32, 8, 36)),
            'bottom': self.image.crop((8, 32, 12, 36))
        }

    @property
    def right_leg_second_front(self) -> Optional[Image.Image]:
        if not self.available_second:
            return None
        return self.image.crop((4, 36, 8, 48))

    @property
    def left_leg(self) -> Dict[str, Image.Image]:
        if self.version == 'old':
            return self.right_leg

        return {
            'front': self.image.crop((20, 52, 24, 64)),
            'back': self.image.crop((28, 52, 32, 64)),
            'left': self.image.crop((16, 52, 20, 64)),
            'right': self.image.crop((24, 52, 28, 64)),
            'top': self.image.crop((20, 48, 24, 52)),
            'bottom': self.image.crop((24, 48, 28, 52))
        }

    @property
    def left_leg_front(self) -> Image.Image:
        if self.version == 'old':
            return self.right_leg_front
        return self.image.crop((20, 52, 24, 64))

    @property
    def left_leg_second(self) -> Optional[Dict[str, Image.Image]]:
        if not self.available_second:
            return None

        return {
            'front': self.image.crop((4, 52, 8, 64)),
            'back': self.image.crop((12, 52, 16, 64)),
            'left': self.image.crop((0, 52, 4, 64)),
            'right': self.image.crop((8, 52, 12, 64)),
            'top': self.image.crop((4, 48, 8, 52)),
            'bottom': self.image.crop((8, 48, 12, 52))
        }

    @property
    def left_leg_second_front(self) -> Optional[Image.Image]:
        if not self.available_second:
            return None
        return self.image.crop((4, 52, 8, 64))

    @property
    def right_hand(self) -> Dict[str, Image.Image]:
        if self.is_slim:
            return {
                'front': self.image.crop((44, 20, 47, 32)),
                'back': self.image.crop((51, 20, 54, 32)),
                'left': self.image.crop((40, 20, 44, 32)),
                'right': self.image.crop((47, 20, 51, 32)),
                'top': self.image.crop((44, 16, 47, 20)),
                'bottom': self.image.crop((47, 16, 51, 20))
            }

        return {
            'front': self.image.crop((44, 20, 48, 32)),
            'back': self.image.crop((52, 20, 56, 32)),
            'left': self.image.crop((40, 20, 44, 32)),
            'right': self.image.crop((48, 20, 52, 32)),
            'top': self.image.crop((44, 16, 48, 20)),
            'bottom': self.image.crop((48, 16, 52, 20))
        }

    @property
    def right_hand_front(self) -> Image.Image:
        if self.is_slim:
            return self.image.crop((44, 20, 47, 32))
        return self.image.crop((44, 20, 48, 32))

    @property
    def right_hand_second(self) -> Optional[Dict[str, Image.Image]]:
        if not self.available_second:
            return None

        if self.is_slim:
            return {
                'front': self.image.crop((44, 36, 47, 48)),
                'back': self.image.crop((51, 36, 54, 48)),
                'left': self.image.crop((40, 36, 44, 48)),
                'right': self.image.crop((47, 36, 51, 48)),
                'top': self.image.crop((44, 32, 47, 36)),
                'bottom': self.image.crop((47, 32, 51, 36))
            }

        return {
            'front': self.image.crop((44, 36, 48, 48)),
            'back': self.image.crop((52, 36, 56, 48)),
            'left': self.image.crop((40, 36, 44, 48)),
            'right': self.image.crop((48, 36, 52, 48)),
            'top': self.image.crop((44, 32, 48, 36)),
            'bottom': self.image.crop((48, 32, 52, 36))
        }

    @property
    def right_hand_second_front(self) -> Optional[Image.Image]:
        if not self.available_second:
            return None

        if self.is_slim:
            return self.image.crop((44, 36, 48, 48))

        return self.image.crop((44, 36, 48, 48))

    @property
    def left_hand(self) -> Dict[str, Image.Image]:
        if self.version == 'old':
            return self.right_hand

        if self.is_slim:
            return {
                'front': self.image.crop((36, 52, 39, 64)),
                'back': self.image.crop((43, 52, 47, 64)),
                'left': self.image.crop((32, 52, 36, 64)),
                'right': self.image.crop((39, 52, 43, 64)),
                'top': self.image.crop((36, 48, 39, 52)),
                'bottom': self.image.crop((39, 48, 43, 52))
            }

        return {
            'front': self.image.crop((36, 52, 40, 64)),
            'back': self.image.crop((44, 52, 48, 64)),
            'left': self.image.crop((32, 52, 36, 64)),
            'right': self.image.crop((40, 52, 44, 64)),
            'top': self.image.crop((36, 48, 40, 52)),
            'bottom': self.image.crop((40, 48, 44, 52))
        }

    @property
    def left_hand_front(self) -> Image.Image:
        if self.version == 'old':
            return self.right_hand_front

        if self.is_slim:
            return self.image.crop((36, 52, 39, 64))

        return self.image.crop((36, 52, 40, 64))

    @property
    def left_hand_second(self) -> Optional[Dict[str, Image.Image]]:
        if not self.available_second:
            return None

        if self.is_slim:
            return {
                'front': self.image.crop((52, 52, 55, 64)),
                'back': self.image.crop((59, 52, 62, 64)),
                'left': self.image.crop((48, 52, 52, 64)),
                'right': self.image.crop((55, 52, 59, 64)),
                'top': self.image.crop((52, 48, 55, 52)),
                'bottom': self.image.crop((55, 48, 59, 52))
            }

        return {
            'front': self.image.crop((52, 52, 56, 64)),
            'back': self.image.crop((60, 52, 64, 64)),
            'left': self.image.crop((48, 52, 52, 64)),
            'right': self.image.crop((56, 52, 60, 64)),
            'top': self.image.crop((52, 48, 56, 52)),
            'bottom': self.image.crop((56, 48, 60, 52))
        }

    @property
    def left_hand_second_front(self) -> Optional[Image.Image]:
        if not self.available_second:
            return None

        if self.is_slim:
            return self.image.crop((52, 52, 55, 64))

        return self.image.crop((52, 52, 56, 64))

    @property
    def body(self) -> Dict[str, Image.Image]:
        return {
            'front': self.image.crop((20, 20, 28, 32)),
            'back': self.image.crop((32, 20, 40, 32)),
            'left': self.image.crop((16, 20, 20, 32)),
            'right': self.image.crop((28, 20, 32, 32)),
            'top': self.image.crop((20, 16, 28, 20)),
            'bottom': self.image.crop((28, 16, 36, 20))
        }

    @property
    def body_front(self) -> Image.Image:
        return self.image.crop((20, 20, 28, 32))

    @property
    def body_second(self) -> Optional[Dict[str, Image.Image]]:
        if not self.available_second:
            return None

        return {
            'front': self.image.crop((20, 36, 28, 48)),
            'back': self.image.crop((32, 36, 40, 48)),
            'left': self.image.crop((16, 36, 20, 48)),
            'right': self.image.crop((28, 36, 32, 48)),
            'top': self.image.crop((20, 32, 28, 36)),
            'bottom': self.image.crop((28, 32, 36, 36))
        }

    @property
    def body_second_front(self) -> Optional[Image.Image]:
        if not self.available_second:
            return None
        return self.image.crop((20, 36, 28, 48))

    @property
    def head(self) -> Dict[str, Image.Image]:
        return {
            'front': self.image.crop((8, 8, 16, 16)),
            'back': self.image.crop((24, 8, 32, 16)),
            'left': self.image.crop((0, 8, 8, 16)),
            'right': self.image.crop((16, 8, 24, 16)),
            'top': self.image.crop((8, 0, 16, 8)),
            'bottom': self.image.crop((16, 0, 24, 8))
        }

    @property
    def head_front(self) -> Image.Image:
        return self.image.crop((8, 8, 16, 16))

    @property
    def head_second(self) -> Optional[Dict[str, Image.Image]]:
        if not self.available_second:
            return None

        return {
            'front': self.image.crop((40, 8, 48, 16)),
            'back': self.image.crop((56, 8, 64, 16)),
            'left': self.image.crop((32, 8, 40, 16)),
            'right': self.image.crop((48, 8, 56, 16)),
            'top': self.image.crop((40, 0, 48, 8)),
            'bottom': self.image.crop((48, 0, 56, 8))
        }

    @property
    def head_second_front(self) -> Optional[Image.Image]:
        if not self.available_second:
            return None
        return self.image.crop((40, 8, 48, 16))
