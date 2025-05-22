---
sidebar_position: 1
---

# Skin

The `Skin` class is a fundamental component of wavy-totem-lib that handles Minecraft skin files and provides methods to access different parts of the skin.

## Overview

Minecraft skins are 64x32 or 64x64 pixel images that define the appearance of a player character. The `Skin` class in wavy-totem-lib loads these images and provides convenient access to different parts of the skin, such as the head, body, arms, and legs, as well as their second layers (overlays).

## Creating a Skin Object

You can create a `Skin` object by providing a path to a skin file:

```python
from wavy_totem_lib import Skin

# From a local file
skin = Skin('path/to/skin.png')

# Specifying if the skin is slim (3-pixel arms) or wide (4-pixel arms)
slim_skin = Skin('path/to/skin.png', slim=True)
```

If you don't specify the `slim` parameter, the library will attempt to detect it automatically based on the skin's pixel data.

## Skin Properties

The `Skin` class provides several properties and methods to access different parts of the skin:

### Basic Properties

- `image`: The original PIL Image object of the skin
- `is_slim`: Boolean indicating whether the skin has slim arms (3 pixels wide) or wide arms (4 pixels wide)
- `available_second`: Boolean indicating whether the skin has a second layer (overlay)

### Body Parts

The `Skin` class provides methods to access different parts of the skin:

#### Head

- `head()`: Returns the head part of the skin
- `head_front()`: Returns the front face of the head
- `head_second()`: Returns the second layer of the head
- `head_second_front()`: Returns the front face of the second layer of the head

#### Body

- `body()`: Returns the body part of the skin
- `body_front()`: Returns the front of the body
- `body_second()`: Returns the second layer of the body
- `body_second_front()`: Returns the front of the second layer of the body

#### Arms

- `right_hand()`: Returns the right arm of the skin
- `right_hand_front()`: Returns the front of the right arm
- `right_hand_second()`: Returns the second layer of the right arm
- `right_hand_second_front()`: Returns the front of the second layer of the right arm
- `left_hand()`: Returns the left arm of the skin
- `left_hand_front()`: Returns the front of the left arm
- `left_hand_second()`: Returns the second layer of the left arm
- `left_hand_second_front()`: Returns the front of the second layer of the left arm

#### Legs

- `right_leg()`: Returns the right leg of the skin
- `right_leg_front()`: Returns the front of the right leg
- `right_leg_second()`: Returns the second layer of the right leg
- `right_leg_second_front()`: Returns the front of the second layer of the right leg
- `left_leg()`: Returns the left leg of the skin
- `left_leg_front()`: Returns the front of the left leg
- `left_leg_second()`: Returns the second layer of the left leg
- `left_leg_second_front()`: Returns the front of the second layer of the left leg

## Minecraft Skin Format

Understanding the Minecraft skin format can help you better understand how the `Skin` class works:

- The skin is divided into different regions that correspond to different parts of the player model
- Each part has a base layer and may have a second layer (overlay)
- The second layer is typically used for details like clothing, accessories, etc.
- Skins can be either "slim" (3-pixel arms) or "wide" (4-pixel arms)

The `Skin` class handles all the complexity of extracting these parts from the skin image, so you don't have to worry about the details of the skin format.

## Usage in TotemBuilder

The `Skin` class is typically used as an input to the `TotemBuilder` class:

```python
from wavy_totem_lib import TotemBuilder, Skin

builder = TotemBuilder(Skin('my_skin.png'))
totem = builder.build()
```

The `TotemBuilder` uses the `Skin` object to extract the necessary parts of the skin to create a totem.