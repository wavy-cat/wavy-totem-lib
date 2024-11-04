from wavy_totem_lib import Skin

with open('skin.png', mode='rb') as file:
    # As an example, we will get the bytes in this way.
    # But they are usually obtained through networking, for example.
    skin_bytes = file.read()

skin = Skin(
    filepath=skin_bytes,
    slim=False  # True, False or ...
)