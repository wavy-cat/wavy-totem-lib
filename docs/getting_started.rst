Getting started
===============

Installation
------------

First, you need to install the library from PyPI.
Please note that this library requires Python 3.8 or higher.

* Using Poetry:

.. code-block:: bash

    poetry add wavy-totem-lib

..

* Using pip:

.. code-block:: bash

    pip install wavy-totem-lib

..

Quick start
-----------

Top-level totem generation is performed using the TotemBuilder.
As an example, you can write code like this:

.. code-block:: python

    from wavy_totem_lib import TotemBuilder, Skin, Totem, ALL_TOP_LAYERS

    builder = TotemBuilder(
        Skin('skin.png'),  # Specify the skin object
        top_layers=ALL_TOP_LAYERS,  # Use all skin top layers
        round_head=True  # Round off the totem's head
    )

    totem = builder.build()  # Generate our totem
    totem.image.save('totem.png')  # And save it into the file

..