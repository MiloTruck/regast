from enum import Enum

class Visibility(str, Enum):
    PUBLIC = 'public'
    PRIVATE = 'private'
    INTERNAL = 'internal'
    EXTERNAL = 'external'

    def __str__(self):
        return self.value

class StateMutability(str, Enum):
    NON_PAYABLE = ''
    PURE = 'pure'
    CONSTANT = 'constant'
    VIEW = 'view'
    PAYABLE = 'payable'

    def __str__(self):
        return self.value