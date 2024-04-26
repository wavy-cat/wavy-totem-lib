#                  Copyright WavyCat 2024.
#  Distributed under the Boost Software License, Version 1.0.
#         (See accompanying file LICENSE or copy at
#           https://www.boost.org/LICENSE_1_0.txt)


class SmallScale(Exception):
    def __init__(self, message: str = 'Cannot increase size to 0x or less'):
        self.message = message
        super().__init__(self.message)
