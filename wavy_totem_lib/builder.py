#                  Copyright WavyCat 2024.
#  Distributed under the Boost Software License, Version 1.0.
#         (See accompanying file LICENSE or copy at
#           https://www.boost.org/LICENSE_1_0.txt)

from asyncio import get_event_loop
from asyncio.events import AbstractEventLoop
from concurrent.futures import ThreadPoolExecutor, Executor
from typing import Type, Optional

from .options import TopLayers, ALL_TOP_LAYERS
from .skin import Skin
from .styles.abstract import AbstractStyle
from .styles.wavy import WavyStyle
from .totem import Totem


class TotemBuilder:
    def __init__(self, skin: Skin, style: Type[AbstractStyle] = WavyStyle,
                 top_layers: list[TopLayers] | None = ALL_TOP_LAYERS, round_head: bool = False):
        self.skin = skin
        self.style = style
        self.top_layers = top_layers if top_layers is not None else []
        self.round_head = round_head

    def build(self, **kwargs) -> Totem:
        totem_image = self.style(self.skin, self.top_layers, **kwargs).image

        if self.round_head:
            # Round the head (if necessary)
            totem_image.putpixel((4, 1), (0, 0, 0, 0))
            totem_image.putpixel((11, 1), (0, 0, 0, 0))

        return Totem(totem_image, self.style, self.skin.is_slim, self.top_layers, self.round_head)

    async def build_async(self, loop: Optional[Type[AbstractEventLoop]] = None,
                          executor: Executor = ThreadPoolExecutor(), **kwargs) -> Totem:
        if not loop:
            loop = get_event_loop()

        return await loop.run_in_executor(executor, lambda: self.build(**kwargs))
