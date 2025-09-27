class SmallScale(Exception):
    def __init__(self, message: str = 'Cannot increase size to 0x or less'):
        self.message = message
        super().__init__(self.message)
