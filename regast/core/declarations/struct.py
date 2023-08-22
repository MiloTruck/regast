from typing import List

from regast.core.core import Core
from regast.core.expressions.identifier import Identifier
from regast.core.variables.struct_member import StructMember
from regast.parsing.ast_node import ASTNode

class Struct(Core):
    def __init__(self, node: ASTNode):
        super().__init__(node)

        self._name: Identifier = None
        self._members: List[StructMember] = []

    @property
    def name(self) -> Identifier:
        return self._name

    @property
    def members(self) -> List[StructMember]:
        return list(self._members)

    @property
    def children(self) -> List:
        return [self.name] + self.members

    def __eq__(self, other):
        if isinstance(other, Struct):
            return self.name == other.name and self.members == other.members
        return False