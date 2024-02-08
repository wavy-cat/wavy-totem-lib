#          Copyright WavyCat 2024 - 2025.
# Distributed under the Boost Software License, Version 1.0.
#        (See accompanying file LICENSE or copy at
#          https://www.boost.org/LICENSE_1_0.txt)

class EmptyTotem(Exception):
    def __init__(self, message: str = 'Totem not generated. Use .generate() method to generate the totem first'):
        self.message = message
        super().__init__(self.message)


class SmallScale(Exception):
    def __init__(self, message: str = 'Cannot increase size to 0x or less'):
        self.message = message
        super().__init__(self.message)
