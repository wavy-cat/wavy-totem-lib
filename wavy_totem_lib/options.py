#          Copyright WavyCat 2024 - 2025.
# Distributed under the Boost Software License, Version 1.0.
#        (See accompanying file LICENSE or copy at
#          https://www.boost.org/LICENSE_1_0.txt)

from enum import Enum


class SkinType(Enum):
    """
    An enumeration class representing the types of skin.

    Attributes:
        WIDE: Represents a wide skin type.
        SLIM: Represents a slim skin type.
        AUTO: Represents automatic detection of a skin type.
    """

    WIDE = 'wide'
    SLIM = 'slim'
    AUTO = 'auto'


class TopLayers(Enum):
    """
    Represents the available options for top layers of skin.

    Attributes:
        NOTHING: Represents the option to have no top layer.
        ALL: Represents the option to have all top layers.
        ONLY_HEAD: Represents the option to have only the head top layer.
        ONLY_TORSO: Represents the option to have only the torso top layer.
        ONLY_HANDS: Represents the option to have only the hands top layer.
        HEAD_AND_TORSO: Represents the option to have both the head and torso top layers.
        HEAD_AND_HANDS: Represents the option to have both the head and hands top layers.
    """

    NOTHING = 0
    ALL = 1
    ONLY_HEAD = 2
    ONLY_TORSO = 3
    ONLY_HANDS = 4
    HEAD_AND_TORSO = 5
    HEAD_AND_HANDS = 6
