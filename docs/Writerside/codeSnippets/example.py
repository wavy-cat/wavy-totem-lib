from wavy_totem_lib import TotemBuilder, Skin, ALL_TOP_LAYERS

builder = TotemBuilder(
    Skin('skin.png'),  # Specify the skin object
    top_layers=ALL_TOP_LAYERS,  # Use all skin top layers
    round_head=True  # Round the head of the totem
)

totem = builder.build()  # Generate our totem
totem.image.save('totem.png')  # And save it into the file
