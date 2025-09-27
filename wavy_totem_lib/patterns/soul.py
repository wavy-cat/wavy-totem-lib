from PIL import Image, ImageOps

from .abstract import Abstract
from ..skin import Skin
from ..layers import TopLayer


class STT(Abstract):
    """
    Pattern by UnFamousSoul (https://github.com/UnFamousSoul).

    See examples at https://totemlib.wavycat.ru/concepts/pattern/#stt
    """

    def __init__(self, skin: Skin, top_layers: list[TopLayer], **kwargs):
        super().__init__(skin, top_layers, **kwargs)

    def _add_head(self):
        self._canvas.paste(self.skin.head_front, (4, 1))

        if self.skin.available_second and TopLayer.HEAD in self.top_layers:
            self._canvas.alpha_composite(self.skin.head_second_front, (4, 1))

    @staticmethod
    def _body(skin, uol):
        body = Image.new("RGBA", (8, 4))

        body.paste(skin.crop((20, 21, 28, 22)), (0, 0))
        body.paste(skin.crop((20, 23, 28, 24)), (0, 1))
        body.paste(skin.crop((20, 29, 28, 30)), (0, 2))
        body.paste(skin.crop((20, 31, 28, 32)), (0, 3))
        if uol:
            l21 = skin.crop((20, 37, 28, 38))
            l22 = skin.crop((20, 39, 28, 40))
            l23 = skin.crop((20, 45, 28, 46))
            l24 = skin.crop((20, 47, 28, 48))
            body.paste(l21, (0, 0), l21)
            body.paste(l22, (0, 1), l22)
            body.paste(l23, (0, 2), l23)
            body.paste(l24, (0, 3), l24)
        return body

    @staticmethod
    def _legs(skin, uol):
        legs = Image.new("RGBA", (6, 3))

        legs.paste(skin.crop((4, 20, 5, 22)), (0, 0))
        legs.paste(skin.crop((6, 20, 8, 22)), (1, 0))
        legs.paste(skin.crop((20, 52, 22, 54)), (3, 0))
        legs.paste(skin.crop((23, 52, 24, 54)), (5, 0))

        legs.paste(skin.crop((4, 31, 5, 32)), (1, 2))
        legs.paste(skin.crop((7, 31, 8, 32)), (2, 2))
        legs.paste(skin.crop((20, 63, 21, 64)), (3, 2))
        legs.paste(skin.crop((23, 63, 24, 64)), (4, 2))
        if uol:
            l21 = skin.crop((4, 36, 5, 38))
            l22 = skin.crop((6, 36, 8, 38))
            l23 = skin.crop((4, 52, 6, 54))
            l24 = skin.crop((7, 52, 8, 54))
            legs.paste(l21, (0, 0), l21)
            legs.paste(l22, (1, 0), l22)
            legs.paste(l23, (3, 0), l23)
            legs.paste(l24, (5, 0), l24)

            l25 = skin.crop((4, 47, 5, 48))
            l26 = skin.crop((7, 47, 8, 48))
            l27 = skin.crop((4, 63, 5, 64))
            l28 = skin.crop((7, 63, 8, 64))
            legs.paste(l25, (1, 2), l25)
            legs.paste(l26, (2, 2), l26)
            legs.paste(l27, (3, 2), l27)
            legs.paste(l28, (4, 2), l28)
        return legs

    @staticmethod
    def _arms(skin, uol, slim):
        arms = Image.new("RGBA", (14, 3))

        arms.paste(skin.crop((37, 52, 39, 54) if slim else (37, 52, 40, 54)).rotate(90, expand=True), (11, 0))
        arms.paste(skin.crop((44, 20, 46, 22) if slim else (44, 20, 47, 22)).rotate(-90, expand=True), (1, 0))
        arms.paste(skin.crop((39, 63, 40, 64)), (13, 0))
        arms.paste(skin.crop((36, 63, 37, 64)), (13, 1))
        arms.paste(skin.crop((44, 31, 45, 32)), (0, 0))
        arms.paste(skin.crop((47, 31, 48, 32)), (0, 1))

        if uol:
            l21 = skin.crop((53, 52, 56, 54)).rotate(90, expand=True)
            l22 = skin.crop((44, 36, 47, 38)).rotate(-90, expand=True)
            l23 = skin.crop((55, 63, 56, 64))
            l24 = skin.crop((52, 63, 53, 64))
            l25 = skin.crop((44, 47, 45, 48))
            l26 = skin.crop((47, 47, 48, 48))

            arms.paste(l21, (11, 0), l21)
            arms.paste(l22, (1, 0), l22)
            arms.paste(l23, (13, 0), l23)
            arms.paste(l24, (13, 1), l24)
            arms.paste(l25, (0, 0), l25)
            arms.paste(l26, (0, 1), l26)

        return arms

    @property
    def image(self) -> Image.Image:
        torso = self._body(self.skin.image, TopLayer.TORSO in self.top_layers)
        legs = self._legs(self.skin.image, TopLayer.LEGS in self.top_layers)
        arms = self._arms(self.skin.image, TopLayer.HANDS in self.top_layers, self.skin.is_slim)

        self._canvas.paste(arms, (1, 8))
        self._canvas.paste(legs, (5, 13))

        if self.skin.version == 'old':
            self._canvas.paste(ImageOps.mirror(self._canvas.crop((0, 0, 8, 16))), (8, 0))

        self._canvas.paste(torso, (4, 9))
        self._add_head()

        return self._canvas
