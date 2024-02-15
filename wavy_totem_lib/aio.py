#          Copyright WavyCat 2024 - 2025.
# Distributed under the Boost Software License, Version 1.0.
#        (See accompanying file LICENSE or copy at
#          https://www.boost.org/LICENSE_1_0.txt)

from asyncio import get_event_loop
from asyncio.events import AbstractEventLoop
from concurrent.futures import ThreadPoolExecutor, Executor
from pathlib import Path
from typing import Union, IO, Optional

from PIL import Image

from .options import SkinType, TopLayers
from .sync import TotemBuilder


class AsyncTotemBuilder(TotemBuilder):
    def __init__(self, file: Union[str, bytes, Path, IO[bytes]], skin_type: SkinType = SkinType.AUTO,
                 top_layers: TopLayers = TopLayers.ALL, round_head: bool = False,
                 loop: Optional[AbstractEventLoop] = None, executor: Executor = ThreadPoolExecutor()):
        """
        An asynchronous wrapper for TotemBuilder.

        :param file: The path or file-like object of the skin image.
               Accepted types: str, bytes, Path, IO[bytes]
        :param skin_type: The type of skin to apply to the image.
               Accepted values: SkinType enum object (default: AUTO)
        :param top_layers: Determines whether to add a 2nd layer to the image.
               Accepted values: TopLayers enum object (default: ALL)
        :param round_head: Determines whether to round the head shape.
               Accepted values: bool (default: False)
        """
        super().__init__(file, skin_type, top_layers, round_head)
        self.loop = loop if loop else get_event_loop()
        self.executor = executor

    async def generate(self) -> Image.Image:
        """
        Generates a ready-made totem image.
        The parameters passed to the __init__ of the class are used.

        :return: The generated image.
        :rtype: Image

        Example usage:
        ```
        totem = TotemBuilder('my_skin.png', SkinType.SLIM, round_head=True)
        totem_image = await totem.generate()
        totem_image.show()
        ```
        """
        img = await self.loop.run_in_executor(self.executor, super().generate)
        return img

    async def scale(self, *, factor: int) -> Image.Image:
        """
        Scales the image by the given factor.

        :param factor: The scaling factor.
        :type factor: int
        :raises EmptyTotem: If the totem is not generated.
        :raises SmallScale: If the scaling factor is less than or equal to zero.
        :return: The scaled image.
        :rtype: Image

        Example usage:
        ```
        totem = TotemBuilder('my_skin.png', SkinType.WIDE)
        await totem.generate() # Using generate() before scale() is mandatory
        totem_image = await totem.scale(factor=16)
        totem_image.show()
        ```
        """
        img = await self.loop.run_in_executor(self.executor, super().scale, factor)
        return img

    async def save(self, filepath: Union[str, bytes, Path, IO[bytes]]):
        """
        An asynchronous file saving wrapper.

        :param filepath: Path or file-like object where the image will be saved.
        :type filepath: Union[str, bytes, Path, IO[bytes]]

        Example usage:
        ```
        totem = TotemBuilder('my_skin.png', SkinType.SLIM)
        await totem.generate()
        await totem.save("totem.png")
        ```
        """
        await self.loop.run_in_executor(self.executor, self.raw.save, filepath)
