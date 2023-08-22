from enum import Enum
from typing import List, Optional

from regast.core.core import Core
from regast.core.expressions.expression import Expression
from regast.core.expressions.identifier import Identifier
from regast.core.types.type import Type
from regast.parsing.ast_node import ASTNode

class DataLocation(str, Enum):
    MEMORY = 'memory'
    STORAGE = 'storage'
    CALLDATA = 'calldata'

    def __str__(self):
        return self.value

class Variable(Core):
    def __init__(self, node: ASTNode):
        super().__init__(node)

        self._type: Type = None
        self._name: Optional[Identifier] = None
        self._data_location: Optional[DataLocation] = None
        self._expression: Optional[Expression] = None

        self._read_references: List[Identifier] = []
        self._write_references: List[Identifier] = []

    @property
    def type(self) -> Type:
        return self._type

    @property
    def name(self) -> Optional[Identifier]:
        return self._name

    @property
    def data_location(self) -> Optional[DataLocation]:
        return self._data_location

    @property
    def initial_expression(self) -> Optional[Expression]:
        return self._expression

    @property
    def is_initialized(self) -> bool:
        return bool(self.initial_expression)

    @property
    def read_references(self) -> List[Identifier]:
        return list(self._read_references)

    @property
    def write_references(self) -> List[Identifier]:
        return list(self.write_references)

    @property
    def references(self) -> List[Identifier]:
        return self.read_references + self.write_references

    @property
    def children(self) -> List:
        return [self.type] + [x for x in [self.name, self.initial_expression] if x]

    def __str__(self):
        s = str(self.type)
        if self.data_location:
            s += ' ' + self.data_location.value
        if self.name:
            s += ' ' + str(self.name)
        if self.is_initialized:
            s += ' = ' + str(self.initial_expression)
        return s

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.type == other.type and self.name == other.name and self.data_location == other.data_location and self.initial_expression == other.initial_expression
        return False
            
