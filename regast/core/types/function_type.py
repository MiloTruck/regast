from typing import List, Optional, Tuple
from regast.core.common import StateMutability, Visibility

from regast.core.types.type import Type
from regast.core.variables.function_type_variable import FunctionTypeVariable
from regast.parsing.ast_node import ASTNode

class FunctionType(Type):
    def __init__(self, node: ASTNode):
        super().__init__(node)

        self._parameters: List[FunctionTypeVariable] = []
        self._return_parameters: List[FunctionTypeVariable] = []
        self._visibility: Optional[Visibility] = None
        self._mutability: Optional[StateMutability] = None

    @property
    def parameters(self) -> List[FunctionTypeVariable]:
        return list(self._parameters)

    @property
    def return_parameters(self) -> List[FunctionTypeVariable]:
        return list(self._return_parameters)

    @property
    def visibility(self) -> Optional[Visibility]:
        return self._visibility

    @property                
    def mutability(self) -> Optional[StateMutability]:
        return self._mutability

    @property
    def storage_size(self) -> Tuple[int, bool]:
        return 24, False

    @property
    def children(self) -> List:
        return self.parameters + self.return_parameters

    def __str__(self):
        s = 'function'
        if self.parameters:
            s += '(' + ', '.join([str(x) for x in self.parameters]) + ')'
        if self.visibility:
            s += ' ' + self.visibility.value
        if self.mutability:
            s += ' ' + self.mutability.value
        if self.return_parameters:
            s += ' returns (' + ', '.join([str(x) for x in self.return_parameters]) + ')'
        return s

    def __eq__(self, other):
        if isinstance(other, FunctionType):
            return self.parameters == other.parameters and self.return_parameters == other.return_parameters and self.visibility == other.visibility and other.mutability == other.mutability
        return False
        