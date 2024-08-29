Totem
=====

Introduction
------------

Totem is a class that represents the texture of the totem and its properties.

Reference
---------

.. automodule:: wavy_totem_lib.totem
   :members:
   :undoc-members:

Examples
--------

Save totem image
~~~~~~~~~~~~~~~~

.. code-block:: python

    from io import BytesIO
    from wavy_totem_lib import TotemBuilder, Skin

    totem = TotemBuilder(Skin('skin.png')).build()  # Create Totem using the builder

    # Save to a file totem.png
    totem.image.save('totem.png')

    # Save to memory (BytesIO)
    virtual_file = BytesIO()
    totem.image.save(virtual_file, format='PNG')

..

Scale totem image
~~~~~~~~~~~~~~~~~

.. code-block:: python

    from wavy_totem_lib import TotemBuilder, Skin

    totem = TotemBuilder(Skin('skin.png')).build()  # Create Totem using the builder

    # Scale texture size by a factor of 10
    image = totem.scale(factor=10)  # `.scale` returns a PIL.Image.Image object

    image.save('totem.png')  # Save

..

Get totem properties
~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    from wavy_totem_lib import TotemBuilder, Skin

    totem = TotemBuilder(Skin('skin.png')).build()  # Create Totem using the builder

    print(
        f'Top layers: {totem.top_layers}',
        f'Style: {totem.style}',
        f'Is the head rounded: {totem.rounded_head}',
        f'Is slim: {totem.slim}',
        sep='\n'
    )

..