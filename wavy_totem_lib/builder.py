from asyncio import get_event_loop
from asyncio.events import AbstractEventLoop
from concurrent.futures import ThreadPoolExecutor, Executor
from typing import Type, Optional

from .layers import TopLayer, ALL_TOP_LAYERS
from .skin import Skin
from .patterns.abstract import Abstract
from .patterns.wavy import Wavy
from .totem import Totem


class TotemBuilder:
    """
    A class designed to obtain the Totem class from Skin using the passed pattern.

    :param skin: The skin object to use for building the totem.
    :param pattern: The pattern class to use for building the totem. Defaults to Wavy.
    :param top_layers: A list of top layers to apply to the totem. Defaults to ALL_TOP_LAYERS.
    :param round_head: Determines whether to round the head or not. Defaults to False.
    """
    def __init__(self, skin: Skin, pattern: Type[Abstract] = Wavy,
                 top_layers: list[TopLayer] | None = ALL_TOP_LAYERS, round_head: bool = False):
        self.skin = skin
        self.pattern = pattern
        self.top_layers = top_layers if top_layers is not None else []
        self.round_head = round_head

    def build(self, **kwargs) -> Totem:
        """
        Builds a totem using the specified parameters.

        :param kwargs: Additional keyword arguments.
        :return: The built Totem object.
        :rtype: Totem
        """
        totem_image = self.pattern(self.skin, self.top_layers, **kwargs).image

        if self.round_head:
            # Round the head (if necessary)
            totem_image.putpixel((4, 1), (0, 0, 0, 0))
            totem_image.putpixel((11, 1), (0, 0, 0, 0))

        return Totem(totem_image, self.pattern, self.skin.is_slim, self.top_layers, self.round_head)

    async def build_async(self, loop: Optional[Type[AbstractEventLoop]] = None,
                          executor: Executor = ThreadPoolExecutor(), **kwargs) -> Totem:
        """
        Asynchronously builds the Totem object.

        :param loop: An optional event loop to be used. If not provided, the default event loop will be used.
        :type loop: Optional[Type[AbstractEventLoop]]
        :param executor: An executor used to run the build method. Default is ThreadPoolExecutor.
        :type executor: Executor
        :param kwargs: Additional keyword arguments.

        :return: The built Totem object.
        :rtype: Totem
        """
        if not loop:
            loop = get_event_loop()

        return await loop.run_in_executor(executor, lambda: self.build(**kwargs))
