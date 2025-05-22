---
sidebar_position: 1
---

# Introduction to TotemLib

**TotemLib** (aka wavy-totem-lib) is a Python library designed to generate totems of undying for Minecraft.
It allows you to create custom totem textures based on Minecraft skin files.

## Features

* Support for 64x32 Minecraft skins
* Zoning of 2 layers and rounding of the head
* Lossless scaling of image size
* Asynchronous support
* Compatible with PyPy
* Multiple built-in styles (Wavy, STT)
* Extensible style system for custom totem designs

## What totem are we talking about?

Refer to [Minecraft.wiki](https://minecraft.wiki/w/Totem_of_Undying) with this question.

## Library Overview

The library consists of several key components:

- **Skin**: Handles Minecraft skin files and provides methods to access different parts of the skin.
- **Totem**: Represents a Minecraft totem texture with methods for scaling and saving.
- **TotemBuilder**: Builds a totem from a skin using a specified style.
- **Styles**: Define how the totem is generated from the skin (WavyStyle, STTStyle, or custom styles).

In the following sections, you'll learn how to install the library, get started with basic usage, explore examples, and
understand the core concepts in detail.
