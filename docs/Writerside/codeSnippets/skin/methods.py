from PIL.Image import Image
from wavy_totem_lib import AbstractStyle, Skin, TopLayer


class CustomStyle(AbstractStyle):
    def __init__(self, skin: Skin, top_layers: list[TopLayer], **kwargs):
        super().__init__(skin, top_layers, **kwargs)

    def _get_left_hand_back(self) -> Image:
        # Here we use the property method of the Skin class
        return self.skin.head['back']
