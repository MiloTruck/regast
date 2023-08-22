from typing import List

from regast.core.core import Core
from regast.core.expressions.identifier import Identifier
from regast.core.variables.error_parameter import ErrorParameter
from regast.parsing.ast_node import ASTNode

class CustomError(Core):
    def __init__(self, node: ASTNode):
        super().__init__(node)

        self._name: Identifier = None
        self._parameters: List[ErrorParameter] = []

    @property
    def name(self) -> Identifier:
        return self._name

    @property
    def parameters(self) -> List[ErrorParameter]:
        return list(self._parameters)

    @property
    def children(self) -> List:
        return [self.name] + self.parameters

    def __eq__(self, other):
        if isinstance(other, CustomError):
            return self.name == other.name and self.parameters == other.parameters
        return False