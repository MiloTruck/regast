from typing import List

from regast.core.expressions.identifier import Identifier
from regast.core.types.type import Type
from regast.parsing.ast_node import ASTNode

class UserDefinedType(Type):
    def __init__(self, node: ASTNode):
        super().__init__(node)

        self._identifiers: List[Identifier] = []

    @property
    def type(self) -> str:
        return ".".join([str(x) for x in self._identifiers])

    def __str__(self):
        return self.type

    def __eq__(self, other):
        if isinstance(other, str):
            return self.type == other
        elif isinstance(other, UserDefinedType):
            return self.type == other.type
        return False