---
title: Totem
description: Learn about the concept of totems
---

Totem — a class that contains the totem image, metadata, and utility methods.

## Properties

* `image`: `PIL.Image` — the totem image.
* `slim`: `bool` — whether the totem is slim or not. Depends on the skin.
* `pattern`: `Type[Abstract]` — the pattern used during totem generation.
* `rounded_head`: `bool` — whether the head is rounded.
* `top_layers`: `list[TopLayer]` — list of enabled top layers on the totem.

## Methods

* `scale(self, *, factor: int)`: `PIL.Image` — method for simple totem scaling by duplicating 1 pixel into n^2 pixels (where n is the provided factor).