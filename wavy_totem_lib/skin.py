#           Copyright WavyCat 2024 - 2025.
#  Distributed under the Boost Software License, Version 1.0.
#         (See accompanying file LICENSE or copy at
#           https://www.boost.org/LICENSE_1_0.txt)

from pathlib import Path
from typing import Union, IO

from PIL import Image


class Skin:
    # TODO: Добавить логику для старого типа скинов
    def __init__(self, filepath: Union[str, bytes, Path, IO[bytes]]):
        self.image: Image.Image = Image.open(filepath)
        self.version = 'new' if self.image.height == 64 else 'old'

    @property
    def right_leg(self) -> dict[str, Image.Image]:
        # Top, Bottom
        # Left, Front, Right, Back
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
    def right_leg_second(self) -> dict[str, Image.Image]:
        return {
            'front': self.image.crop((4, 36, 8, 48)),
            'back': self.image.crop((12, 36, 16, 48)),
            'left': self.image.crop((0, 36, 4, 48)),
            'right': self.image.crop((8, 36, 12, 48)),
            'top': self.image.crop((4, 32, 8, 36)),
            'bottom': self.image.crop((8, 32, 12, 36))
        }

    @property
    def right_leg_second_front(self) -> Image.Image:
        return self.image.crop((4, 36, 8, 48))

    @property
    def left_leg(self) -> dict[str, Image.Image]:
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
        return self.image.crop((20, 52, 24, 64))

    @property
    def left_leg_second(self) -> dict[str, Image.Image]:
        return {
            'front': self.image.crop((4, 52, 8, 64)),
            'back': self.image.crop((12, 52, 16, 64)),
            'left': self.image.crop((0, 52, 4, 64)),
            'right': self.image.crop((8, 52, 12, 64)),
            'top': self.image.crop((4, 48, 8, 52)),
            'bottom': self.image.crop((8, 48, 12, 52))
        }

    @property
    def left_leg_second_front(self) -> Image.Image:
        return self.image.crop((4, 52, 8, 64))

    @property
    def right_hand(self) -> dict[str, Image.Image]:
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
        return self.image.crop((44, 20, 48, 32))

    @property
    def right_hand_second(self) -> dict[str, Image.Image]:
        return {
            'front': self.image.crop((44, 36, 48, 48)),
            'back': self.image.crop((52, 36, 56, 48)),
            'left': self.image.crop((40, 36, 44, 48)),
            'right': self.image.crop((48, 36, 52, 48)),
            'top': self.image.crop((44, 32, 48, 36)),
            'bottom': self.image.crop((48, 32, 52, 36))
        }

    @property
    def right_hand_second_front(self) -> Image.Image:
        return self.image.crop((44, 36, 48, 48))

    @property
    def left_hand(self) -> dict[str, Image.Image]:
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
        return self.image.crop((36, 52, 40, 64))

    @property
    def left_hand_second(self) -> dict[str, Image.Image]:
        return {
            'front': self.image.crop((52, 52, 56, 64)),
            'back': self.image.crop((60, 52, 64, 64)),
            'left': self.image.crop((48, 52, 52, 64)),
            'right': self.image.crop((56, 52, 60, 64)),
            'top': self.image.crop((52, 48, 56, 52)),
            'bottom': self.image.crop((56, 48, 60, 52))
        }

    @property
    def left_hand_second_front(self) -> Image.Image:
        return self.image.crop((52, 52, 56, 64))

    @property
    def body(self) -> dict[str, Image.Image]:
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
    def body_second(self) -> dict[str, Image.Image]:
        return {
            'front': self.image.crop((20, 36, 28, 48)),
            'back': self.image.crop((32, 36, 40, 48)),
            'left': self.image.crop((16, 36, 20, 48)),
            'right': self.image.crop((28, 36, 32, 48)),
            'top': self.image.crop((20, 32, 28, 36)),
            'bottom': self.image.crop((28, 32, 36, 36))
        }

    @property
    def body_second_front(self) -> Image.Image:
        return self.image.crop((20, 36, 28, 48))

    @property
    def head(self) -> dict[str, Image.Image]:
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
    def head_second(self) -> dict[str, Image.Image]:
        return {
            'front': self.image.crop((40, 8, 48, 16)),
            'back': self.image.crop((56, 8, 64, 16)),
            'left': self.image.crop((32, 8, 40, 16)),
            'right': self.image.crop((48, 8, 56, 16)),
            'top': self.image.crop((40, 0, 48, 8)),
            'bottom': self.image.crop((48, 0, 56, 8))
        }

    @property
    def head_second_front(self) -> Image.Image:
        return self.image.crop((40, 8, 48, 16))


# if __name__ == '__main__':
#     a = Skin('../dev/1_8_texturemap_redux.png').right_hand
#     a['left'].save('../dev/left.png')
#     a['right'].save('../dev/right.png')
#     a['front'].save('../dev/front.png')
#     a['back'].save('../dev/back.png')
#     a['top'].save('../dev/top.png')
#     a['bottom'].save('../dev/bottom.png')
