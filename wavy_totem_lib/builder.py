#                  Copyright WavyCat 2024.
#  Distributed under the Boost Software License, Version 1.0.
#         (See accompanying file LICENSE or copy at
#           https://www.boost.org/LICENSE_1_0.txt)

from asyncio import get_event_loop
from asyncio.events import AbstractEventLoop
from concurrent.futures import ThreadPoolExecutor, Executor
from typing import Type, Optional

from .options import TopLayer, ALL_TOP_LAYERS
from .skin import Skin
from .styles.abstract import AbstractStyle
from .styles.wavy import WavyStyle
from .totem import Totem


class TotemBuilder:
    """
    A class designed to obtain the Totem class from Skin using the passed style.

    :param skin: The skin object to use for building the totem.
    :type skin: Skin
    :param style: The style class to use for building the totem. Defaults to WavyStyle.
    :type style: Type[AbstractStyle], optional
    :param top_layers: A list of top layers to apply to the totem. Defaults to ALL_TOP_LAYERS.
    :type top_layers: list[TopLayers] | None, optional
    :param round_head: Determines whether to round the head or not. Defaults to False.
    :type round_head: bool, optional
    """
    def __init__(self, skin: Skin, style: Type[AbstractStyle] = WavyStyle,
                 top_layers: list[TopLayer] | None = ALL_TOP_LAYERS, round_head: bool = False):
        self.skin = skin
        self.style = style
        self.top_layers = top_layers if top_layers is not None else []
        self.round_head = round_head

    def build(self, **kwargs) -> Totem:
        """
        Builds a totem using the specified parameters.

        :param kwargs: Additional keyword arguments.
        :return: The built Totem object.
        :rtype: Totem
        """
        totem_image = self.style(self.skin, self.top_layers, **kwargs).image

        if self.round_head:
            # Round the head (if necessary)
            totem_image.putpixel((4, 1), (0, 0, 0, 0))
            totem_image.putpixel((11, 1), (0, 0, 0, 0))

        return Totem(totem_image, self.style, self.skin.is_slim, self.top_layers, self.round_head)

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
