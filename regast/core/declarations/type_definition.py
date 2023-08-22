from typing import List
from regast.core.core import Core
from regast.core.expressions.identifier import Identifier
from regast.core.types.type import Type
from regast.parsing.ast_node import ASTNode

class TypeDefinition(Core):
    def __init__(self, node: ASTNode):
        super().__init__(node)

        self._alias: Identifier = None
        self._type: Type = None

    @property
    def alias(self) -> Identifier:
        return self._alias

    @property
    def type(self) -> Type:
        return self._type

    @property
    def children(self) -> List:
        return [self.alias, self.type]

    def __eq__(self, other):
        if isinstance(other, TypeDefinition):
            return self.alias == other.alias and self.type == other.type
        return False