Builder
=======

Introduction
------------

The Builder is a high-level class capable of creating a totem object using a skin and the low-level generation method of the given style as a foundation.

The Builder provides both synchronous and asynchronous methods for totem generation.

Reference
---------

.. automodule:: wavy_totem_lib.builder
   :members:
   :undoc-members:

Examples
--------

Synchronous generation
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    from wavy_totem_lib import TotemBuilder, Skin, Totem, ALL_TOP_LAYERS

    builder = TotemBuilder(
        Skin('skin.png'),  # Specify the skin object
        top_layers=ALL_TOP_LAYERS,  # Use all skin top layers
        round_head=True  # Round off the totem's head
    )

    totem = builder.build()  # Generate our totem
    # Yes, this is an example from Getting Started

..

Asynchronous generation
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    import asyncio

    from wavy_totem_lib import TotemBuilder, Skin, TopLayer, STTStyle

    async def main():
        builder = TotemBuilder(
            Skin('skin.png', slim=True),  # Specify the skin object
            style=STTStyle,  # Pass the desired style
            top_layers=[TopLayer.HEAD, TopLayer.TORSO, TopLayer.LEGS]  # Specify which top layers to use
        )
        totem = await builder.build_async()  # Generate the totem asynchronously

    asyncio.run(main())

..