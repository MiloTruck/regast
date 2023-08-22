from enum import Enum
from typing import List, Optional

from regast.core.common import Visibility
from regast.core.types.user_defined_type import UserDefinedType
from regast.core.variables.variable import Variable
from regast.parsing.ast_node import ASTNode

class StateVariableMutability(str, Enum):
    MUTABLE = ''
    IMMUTABLE = 'immutable'
    CONSTANT = 'constant'

    def __str__(self):
        return self.value

class StateVariable(Variable):
    def __init__(self, node: ASTNode):
        super().__init__(node)

        self._visibility: Optional[Visibility] = None
        self._mutability: Optional[StateVariableMutability] = None
        self._override: bool = False
        self._overrides: List[UserDefinedType] = []

    @property    
    def visibility(self) -> Visibility:
        if self._visibility:
            return self._visibility
        return Visibility.PUBLIC

    @property
    def declared_visibility(self) -> Optional[Visibility]:
        """
        This is used to differentiate state variables explicitly declared public
        """
        return self._visibility

    @property
    def mutability(self) -> StateVariableMutability:
        if self._mutability:
            return self._mutability
        return StateVariableMutability.MUTABLE

    @property
    def declared_mutability(self) -> Optional[StateVariableMutability]:
        return self._mutability

    @property
    def is_override(self) -> bool:
        return self._override

    @property
    def overrides(self) -> List[UserDefinedType]:
        return list(self._overrides)

    @property
    def children(self) -> List:
        return self.overrides + super().children

    def __str__(self):
        s = str(self.type)
        if self.declared_visibility:
            s += " " + self.declared_visibility
        if self.mutability != StateVariableMutability.MUTABLE:
            s += " " + self.mutability.value
        if self.overrides:
            s += " override (" + ", ".join([str(x) for x in self.overrides]) + ")"
        s += ' ' + str(self.name)
        if self.is_initialized:
            s += " = " + str(self.initial_expression)    
        return s

    def __eq__(self, other):
        if isinstance(other, StateVariable):
            return self.type == other.type and self.name == other.name and self.declared_visibility == other.declared_visibility and self.mutability == other.mutability and self.overrides == other.overrides and self.initial_expression == other.initial_expression
        return False 