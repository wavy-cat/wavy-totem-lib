# Skin

`Skin` is a class that represents a player's skin.

The constructor for this class accepts a skin (`filepath`) and a boolean indicating whether the skin is slim (`slim`). If the second argument is omitted, the default value `Ellipsis` is used, which instructs the constructor to automatically determine the skin type.

A skin can be:

- A path to a JPG or PNG image,
- A set of image bytes (`bytes` class),
- Other data types supported by [`PIL.Image.open()`](https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.open).

In addition to storing the original skin in RGBA format, the class also keeps parameters like:

- Skin version (`version`): `new` for newer skins (64x64) and `old` for older skins (64x32),
- Second layer availability (`available_second`), which depends on the skin version,
- Slim skin status (`is_slim`),
- Various property methods for accessing specific skin areas (e.g., the left arm of the second layer).

## Property Methods

*Property methods for skin area extraction* allow individual parts of the skin, like limbs or the torso, to be retrieved as image fragments.

Each method is designed to extract a specific part of the layout.

These methods make style development significantly more efficient.

## Use Cases

Creating an instance of the Skin class:

<tabs>
    <tab id="poetry-install" title="File Path">
        <code-block lang="python" src="skin/create.py"/>
    </tab>
    <tab id="pip-install" title="Bytes Object">
        <code-block lang="python" src="skin/create_bytes.py"/>
    </tab>
</tabs>

Obtaining the back of the left arm in a style method:

```python
```
{ src="skin/methods.py" }

## Related Resources

- [Skin on Minecraft.Wiki](https://minecraft.wiki/w/Skin)