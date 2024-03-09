#          Copyright WavyCat 2024 - 2025.
# Distributed under the Boost Software License, Version 1.0.
#        (See accompanying file LICENSE or copy at
#          https://www.boost.org/LICENSE_1_0.txt)

__title__ = "wavy-totem-lib"
__author__ = "WavyCat"
__license__ = "BSL-1.0"
__version__ = ""

from .sync import TotemBuilder
from .aio import AsyncTotemBuilder
from .options import SkinType, TopLayers

from .styles.wavy import WavyStyle
from .styles.soul import STTStyle
from .styles.abstract import AbstractStyle
