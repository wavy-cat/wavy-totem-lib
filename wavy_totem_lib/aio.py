#          Copyright WavyCat 2024 - 2025.
# Distributed under the Boost Software License, Version 1.0.
#        (See accompanying file LICENSE or copy at
#          https://www.boost.org/LICENSE_1_0.txt)

from asyncio import get_event_loop
from asyncio.events import AbstractEventLoop
from concurrent.futures import ThreadPoolExecutor, Executor
from pathlib import Path
from typing import Union, IO, Optional, Type

from PIL import Image

from .options import SkinType, TopLayers
from .styles.abstract import AbstractStyle
from .styles.wavy import WavyStyle
from .sync import TotemBuilder
from string import ascii_lowercase


class AsyncTotemBuilder(TotemBuilder):
    def __init__(self, file: Union[str, bytes, Path, IO[bytes]],
                 style: Type[AbstractStyle] = WavyStyle,
                 skin_type: SkinType = SkinType.AUTO,
                 top_layers: TopLayers = TopLayers.ALL,
                 round_head: bool = False,
                 loop: Optional[AbstractEventLoop] = None,
                 executor: Executor = ThreadPoolExecutor()):
        """
        An asynchronous wrapper for TotemBuilder.

        Args:
            file: The path or file-like object of the skin image.
            style: A class representing a generation style.
            skin_type: The type of skin to apply to the image.
            top_layers: Determines whether to add an outer layer to the image.
            round_head: Determines whether to round the head shape.
            loop: The event loop used by the asyncio library
            executor

        Example:
            ```
            totem = AsyncTotemBuilder('my_skin.png')
            await totem.generate()
            await totem.scale(10)
            await totem.save("totem.png")
            ```
        """

        super().__init__(file, style, skin_type, top_layers, round_head)
        self.loop = loop if loop else get_event_loop()
        self.executor = executor

    async def generate(self, **kwargs) -> Image.Image:
        """
        This method generates a totem image using.
        Additional customization can be done by passing keyword arguments (**kwargs) to the method
        (possible options depend on style).
        The generated image will be stored in the `raw` attribute of the object and will also be returned by the method.

        :param kwargs: Additional keyword arguments to customize the created image.
        :return: The generated image.
        """

        return await self.loop.run_in_executor(self.executor, lambda: super().generate(**kwargs))

    async def scale(self, *, factor: int) -> Image.Image:
        """
        Scales the image by the given factor.

        Args:
            factor: The scaling factor.

        Raises:
            EmptyTotem: If the totem has not yet been generated.
            SmallScale: If the scaling factor is less than 1.

        Example:
            ```
            totem = AsyncTotemBuilder('my_skin.png')
            await totem.generate()
            await totem.scale(factor=10) # 16 × 10 = 160px
            ```

        Returns:
            PIL.Image.Image: Generated totem image
        """

        return await self.loop.run_in_executor(self.executor, super().scale, factor)

    async def save(self, filepath: Union[str, bytes, Path, IO[bytes]]):
        """
        An asynchronous file saving wrapper.

        :param filepath: Path or file-like object where the image will be saved.
        :type filepath: Union[str, bytes, Path, IO[bytes]]

        Example usage:
        ```
        totem = AsyncTotemBuilder('my_skin.png')
        await totem.generate()
        await totem.save("totem.png")
        ```
        """

        await self.loop.run_in_executor(self.executor, self.raw.save, filepath)
