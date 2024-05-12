#                  Copyright WavyCat 2024.
#  Distributed under the Boost Software License, Version 1.0.
#         (See accompanying file LICENSE or copy at
#           https://www.boost.org/LICENSE_1_0.txt)

__title__ = "wavy-totem-lib"
__author__ = "WavyCat"
__license__ = "BSL-1.0"
__version__ = ""

from .builder import TotemBuilder
from .totem import Totem
from .skin import Skin
from .options import TopLayer, ALL_TOP_LAYERS

from .styles.wavy import WavyStyle
from .styles.soul import STTStyle
from .styles.abstract import AbstractStyle
