from typing import List

from regast.core.core import Core
from regast.core.expressions.identifier import Identifier
from regast.parsing.ast_node import ASTNode

class Enum(Core):
    def __init__(self, node: ASTNode):
        super().__init__(node)

        self._name: Identifier = None
        self._values: List[Identifier] = []

    @property
    def name(self) -> Identifier:
        return self._name

    @property
    def values(self) -> List[Identifier]:
        return list(self._values)

    @property
    def children(self) -> List:
        return [self.name] + self.values

    def __eq__(self, other):
        if isinstance(other, Enum):
            return self.name == other.name and self.values == other.values
        return False