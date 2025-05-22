---
sidebar_label: 'Architecture'
sidebar_position: 5
---

# Architecture

This page provides an overview of the TotemLib architecture and how the different components work together.

## Component Overview

TotemLib consists of several key components that work together to generate totem textures:

- **Skin**: Loads and processes Minecraft skin files
- **TotemBuilder**: Configures and orchestrates the totem generation process
- **Styles**: Define how the skin is transformed into a totem
- **Totem**: Represents the final generated totem texture

## Component Relationships

Here's how these components interact:

1. The **Skin** class loads a Minecraft skin file and provides methods to access its different parts.
2. The **TotemBuilder** takes a Skin object and configuration options.
3. When `build()` is called, the TotemBuilder creates a Style instance (WavyStyle, STTStyle, or a custom style).
4. The Style uses the Skin to generate a totem image.
5. The TotemBuilder creates a Totem object with the generated image and configuration.
6. The Totem can be scaled and saved as needed.

## Data Flow

The data flow in TotemLib follows this pattern:

```
Minecraft Skin File → Skin → TotemBuilder → Style → Totem → Final Image
```

## Extensibility

TotemLib is designed to be extensible:

- You can create custom styles by inheriting from AbstractStyle
- The TotemBuilder accepts additional keyword arguments that are passed to the style
- The Totem class provides methods for further processing the generated image

This architecture allows for a high degree of customization while maintaining a simple API for basic use cases.
