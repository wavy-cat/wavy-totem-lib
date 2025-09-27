from enum import Enum


class TopLayer(Enum):
    """
    Represents the available options for top layers of skin.
    Available values: HEAD, TORSO, HANDS, LEGS.
    """

    HEAD = 2 << 2
    TORSO = 2 << 3
    HANDS = 2 << 4
    LEGS = 2 << 5


ALL_TOP_LAYERS = [TopLayer.HEAD, TopLayer.TORSO, TopLayer.HANDS, TopLayer.LEGS]
