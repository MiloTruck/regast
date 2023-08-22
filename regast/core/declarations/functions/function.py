from typing import List, Optional

from regast.core.core import Core
from regast.core.declarations.functions.function_body import FunctionBody
from regast.core.expressions.expression import Expression
from regast.core.expressions.identifier import Identifier
from regast.core.expressions.struct_expression import StructArguments
from regast.core.types.user_defined_type import UserDefinedType
from regast.core.variables.parameter import Parameter
from regast.core.common import Visibility, StateMutability
from regast.parsing.ast_node import ASTNode

class ModifierInvocation(Core):
    def __init__(self, node: ASTNode):
        super().__init__(node)

        self._identifiers: List[Identifier] = []
        self._arguments: List[Expression] = []
        self._struct_arguments: Optional[StructArguments] = None

    @property
    def name(self) -> str:
        return ".".join([str(x) for x in self._identifiers])

    @property
    def struct_arguments(self) -> Optional[StructArguments]:
        return self._struct_arguments

    @property
    def arguments(self) -> List[Expression]:
        return list(self._arguments)

    @property
    def children(self) -> List:
        children = self._identifiers + self.arguments
        if self.struct_arguments:
            children.append(self.struct_arguments)
        return children

    def __eq__(self, other):
        if isinstance(other, ModifierInvocation):
            return (
                self.name == other.name and
                self.struct_arguments == other.struct_arguments and
                self.arguments == other.arguments
            )
        return False

class Function(FunctionBody):
    def __init__(self, node: ASTNode):
        super().__init__(node)

        self._name: Optional[Identifier] = None
        
        self._parameters: List[Parameter] = []
        self._return_parameters: List[Parameter] = []
        self._modifiers: List[ModifierInvocation] = []

        self._visibility: Optional[Visibility] = None
        self._mutability: Optional[StateMutability] = None

        self._virtual: bool = False
        self._override: bool = False
        self._overrides: List[UserDefinedType] = []

    @property
    def name(self) -> Optional[Identifier]:
        return self._name

    @property
    def parameters(self) -> List[Parameter]:
        return list(self._parameters)
        
    @property
    def return_parameters(self) -> List[Parameter]:
        return list(self._return_parameters)

    @property
    def modifiers(self) -> List[ModifierInvocation]:
        return list(self._modifiers)

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
    def mutability(self) -> StateMutability:
        if self._mutability:
            return self._mutability
        return StateMutability.NON_PAYABLE

    @property
    def declared_mutability(self) -> Optional[StateMutability]:
        return self._mutability

    @property
    def is_virtual(self) -> bool:
        return self._virtual

    @property
    def is_override(self) -> bool:
        return self._override

    @property
    def overrides(self) -> List[UserDefinedType]:
        return list(self._overrides)

    @property
    def children(self) -> List:
        children = self.parameters + self.return_parameters
        children += self.modifiers
        children += self.overrides
        if self.name:
            children.append(self.name)
        if self.body:
            children.append(self.body)
        return children

    def __eq__(self, other):
        if isinstance(other, Function):
            return (
                self.name == other.name and 
                self.parameters == other.parameters and 
                self.return_parameters == other.return_parameters and 
                self.modifiers == other.modifiers and 
                self.visibility == other.visibility and
                self.mutability == other.mutability and
                self.is_virtual == other.is_virtual and 
                self.is_override == other.is_override and 
                self.overrides == other.overrides
            )
        return False