#          Copyright WavyCat 2024 - 2025.
# Distributed under the Boost Software License, Version 1.0.
#        (See accompanying file LICENSE or copy at
#          https://www.boost.org/LICENSE_1_0.txt)

from abc import ABC, abstractmethod

from PIL import Image

from ..options import SkinType, TopLayers


class AbstractStyle(ABC):
    """Abstract style class. Use to create other styles."""

    @abstractmethod
    def __init__(self, skin: Image.Image, skin_type: SkinType, top_layers: TopLayers, **kwargs):
        """
        Initializing method.

        Args:
            skin: PIL.Image.Image
            skin_type: SkinType
            top_layers: TopLayers
            **_kwargs - extra options
        """
        self._source = skin  # Skin Image object
        self._skin_type = skin_type
        self._top_layers = top_layers
        self._kwargs = kwargs
        self._canvas = Image.new("RGBA", (16, 16))

    @property
    @abstractmethod
    def image(self) -> Image.Image:
        raise "This is an abstract method, don't try to use it."
