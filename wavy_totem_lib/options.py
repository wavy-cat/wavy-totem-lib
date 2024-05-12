#                  Copyright WavyCat 2024.
#  Distributed under the Boost Software License, Version 1.0.
#         (See accompanying file LICENSE or copy at
#           https://www.boost.org/LICENSE_1_0.txt)

from enum import Enum


class TopLayer(Enum):
    """
    Represents the available options for top layers of skin.
    Available values: HEAD, TORSO, HANDS, LEGS.
    """

    HEAD = 8
    TORSO = 24
    HANDS = 32
    LEGS = 48


ALL_TOP_LAYERS = [TopLayer.HEAD, TopLayer.TORSO, TopLayer.HANDS, TopLayer.LEGS]
