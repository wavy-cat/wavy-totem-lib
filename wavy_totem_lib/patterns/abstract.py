from abc import ABC, abstractmethod

from PIL import Image

from ..layers import TopLayer
from ..skin import Skin


class Abstract(ABC):
    """
    Abstract pattern class.
    Use to create other patterns.
    """

    @abstractmethod
    def __init__(self, skin: Skin, top_layers: list[TopLayer], **kwargs):
        """
        Initializing method. It already contains the declaration of the necessary variables from the parameters.
        In child methods you can use `super().__init__(skin, top_layers, **kwargs)`.

        :param skin: Skin class object
        :rtype skin: Skin
        :param top_layers: List including required second layers
        :rtype top_layers: list[TopLayer]
        :param: **kwargs: Extra options
        """
        self.skin = skin
        self.top_layers = top_layers
        self.kwargs = kwargs
        self._canvas = Image.new("RGBA", (16, 16))

    @property
    @abstractmethod
    def image(self) -> Image.Image:
        """
        The main method with the @property decorator that generates the totem.
        :return: PIL.Image.Image
        """
        raise "This is an abstract method, don't try to use it."
