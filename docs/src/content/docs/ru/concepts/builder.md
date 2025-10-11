---
title: Билдер
description: Изучите концепцию билдера (сборщика) тотема
---

Билдер (он же TotemBuilder) — это вспомогательный класс, который оборачивает все компоненты библиотеки и предоставляет
удобный метод для генерации тотема `build()`.

## Использование

```py
from wavy_totem_lib import TotemBuilder, Skin, TopLayer
from wavy_totem_lib.patterns import STT

builder = TotemBuilder(
    skin=Skin('my_skin.png', slim=True),
    pattern=STT,  # Указание паттерна
    top_layers=[TopLayer.HEAD, TopLayer.HANDS],  # Указание для каких частей тела отображать верхний слой 
    round_head=True  # Указание, нужно ли закруглять голову
)

# Генерация тотема
totem = builder.build()
```

Билдер принимает несколько аргументов:

* `skin`: `Skin` - объект вашего [скина](/ru/concepts/skin/). Это единственный обязательный аргумент;
* `pattern`: `Type[Abstract]` (по-умолчанию [Wavy](/ru/concepts/pattern/#wavy)) - необходимый [паттерн](/ru/concepts/pattern),
  который будет использовать для генерации тотема;
* `top_layers`: `list[TopLayer] | None` (по-умолчанию ALL_TOP_LAYERS) - список
  частей тела enum типа TopLayer, для которых необходимо отобразить верхний слой. Если верхний слой не
  нужен, то передайте пустой список или None. Этот список передаётся в паттерн, сам билдер ничего с ним не делает.
* `round_head`: `bool` (по-умолчанию False) - указывает необходимо ли "закруглить" голову, т.е. убрать 2 верхних пикселя
  по краям головы. Этот функционал реализует сам билдер. Наглядный пример:

| Без закругления                                                                           | С закруглением                                                                         |
|-------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| ![Notch. Пример закругления головы.](../../../../assets/examples/builder/no-rounded.webp) | ![Notch. Пример закругления головы.](../../../../assets/examples/builder/rounded.webp) |

Билдер возвращает экземпляр класса [Totem](/ru/concepts/totem).

### Асинхронное использование

В асинхронном коде вы можете использовать метод `build_async()`, вместо синхронного `build()`.
Де-факто, этот метод является асинхронной обёрткой над `build()`.

```py
from wavy_totem_lib import TotemBuilder, Skin, TopLayer
from wavy_totem_lib.patterns import STT


async def build_totem():
    builder = TotemBuilder(
        skin=Skin('my_skin.png', slim=True),
        pattern=STT,
        top_layers=[TopLayer.HEAD, TopLayer.HANDS],
        round_head=True
    )

    # Асинхронная генерация тотема
    totem = await builder.build_async()
```
