#                  Copyright WavyCat 2024.
#  Distributed under the Boost Software License, Version 1.0.
#         (See accompanying file LICENSE or copy at
#           https://www.boost.org/LICENSE_1_0.txt)

from abc import ABC, abstractmethod

from PIL import Image

from ..options import TopLayers
from ..skin import Skin


class AbstractStyle(ABC):
    """Abstract style class. Use to create other styles."""

    @abstractmethod
    def __init__(self, skin: Skin, top_layers: list[TopLayers], **kwargs):
        """
        Initializing method.

        Args:
            skin: PIL.Image.Image
            top_layers: list[TopLayers]
            **kwargs - extra options
        """
        self.skin = skin
        self.top_layers = top_layers
        self.kwargs = kwargs
        self._canvas = Image.new("RGBA", (16, 16))

    @property
    @abstractmethod
    def image(self) -> Image.Image:
        raise "This is an abstract method, don't try to use it."
