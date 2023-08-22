from typing import List, Optional

from regast.core.core import Core
from regast.core.declarations.custom_error import CustomError
from regast.core.declarations.enum import Enum
from regast.core.declarations.event import Event
from regast.core.declarations.functions.constructor import Constructor
from regast.core.declarations.functions.fallback_function import FallbackFunction
from regast.core.declarations.functions.function import Function
from regast.core.declarations.functions.modifier import Modifier
from regast.core.declarations.functions.receive_function import ReceiveFunction
from regast.core.declarations.struct import Struct
from regast.core.declarations.type_definition import TypeDefinition
from regast.core.declarations.directives.using_directive import UsingDirective
from regast.core.expressions.expression import Expression
from regast.core.expressions.identifier import Identifier
from regast.core.expressions.struct_expression import StructArguments
from regast.core.types.user_defined_type import UserDefinedType
from regast.core.variables.state_variable import StateVariable
from regast.parsing.ast_node import ASTNode


class InheritanceSpecifier(Core):
    def __init__(self, node: ASTNode):
        super().__init__(node)

        self._name: UserDefinedType = None
        self._struct_arguments: Optional[StructArguments] = None
        self._arguments: List[Expression] = []

    @property
    def name(self) -> UserDefinedType:
        return self._name

    @property
    def struct_arguments(self) -> Optional[StructArguments]:
        return self._struct_arguments

    @property
    def arguments(self) -> List[Expression]:
        return list(self._arguments)

    @property
    def children(self):
        children = [self.name] + self.arguments
        if self.struct_arguments:
            children.append(self.struct_arguments)
            
        return children

    def __eq__(self, other):
        if isinstance(other, InheritanceSpecifier):
            return (
                self.name == other.name and
                self.struct_arguments == other.struct_arguments and
                self.arguments == other.arguments
            )
        return False

class Contract(Core):
    def __init__(self, node: ASTNode):
        super().__init__(node)
        
        self._name: Identifier = None
        self._abstract: bool = False
        self._inheritance_specifiers: List[InheritanceSpecifier] = []

        self._constructor: Optional[Constructor] = None
        self._fallback_function: Optional[FallbackFunction] = None
        self._receive_function: Optional[ReceiveFunction] = None
        self._functions: List[Function] = []
        self._modifiers: List[Modifier] = []

        self._structs: List[Struct] = []
        self._enums: List[Enum] = []
        self._type_definitions: List[TypeDefinition] = []
        self._state_variables: List[StateVariable] = []
        self._events: List[Event] = []
        self._custom_errors: List[CustomError] = []
        self._using_directives: List[UsingDirective] = []

    @property
    def name(self) -> Identifier:
        return self._name
        
    @property
    def inheritance_specifiers(self) -> List[InheritanceSpecifier]:
        return list(self._inheritance_specifiers)
        
    @property
    def is_abstract(self) -> bool:
        return self._abstract
        
    @property
    def constructor(self) -> Optional[Constructor]:
        return self._constructor
        
    @property
    def fallback_function(self) -> Optional[FallbackFunction]:
        return self._fallback_function
        
    @property
    def receive_function(self) -> Optional[ReceiveFunction]:
        return self._receive_function
        
    @property
    def functions(self) -> List[Function]:
        return list(self._functions)
        
    @property
    def modifiers(self) -> List[Modifier]:
        return list(self._modifiers)

    @property
    def all_functions(self) -> List[Function]:
        """
        All functions, inclusive of modifiers, constructor, receive and fallback functions
        """
        return self.functions + self.modifiers + [x for x in [self.constructor, self.fallback_function, self.receive_function] if x]
        
    @property
    def structs(self) -> List[Struct]:
        return list(self._structs)
        
    @property
    def enums(self) -> List[Enum]:
        return list(self._enums)
        
    @property
    def type_definitions(self) -> List[TypeDefinition]:
        return list(self._type_definitions)
        
    @property
    def state_variables(self) -> List[StateVariable]:
        return list(self._state_variables)
        
    @property
    def events(self) -> List[Event]:
        return list(self._events)
        
    @property
    def custom_errors(self) -> List[CustomError]:
        return list(self._custom_errors)
        
    @property
    def using_directives(self) -> List[UsingDirective]:
        return list(self._using_directives)

    @property
    def children(self) -> List:
        children = [self.name]

        children += [x for x in [
            self.constructor,
            self.fallback_function,
            self.receive_function
        ] if x]

        children += self.inheritance_specifiers
        children += self.functions + self.modifiers
        children += self.structs + self.enums
        children += self.type_definitions
        children += self.state_variables
        children += self.events
        children += self.custom_errors
        children += self.using_directives

        return children

    def __eq__(self, other):
        if isinstance(other, Contract):
            return (
                self.name == other.name and
                self.inheritance_specifiers == other.inheritance_specifiers and
                self.is_abstract == other.is_abstract and
                self.constructor == other.constructor and
                self.fallback_function == other.fallback_function and
                self.receive_function == other.receive_function and
                self.functions == other.functions and
                self.modifiers == other.modifiers and
                self.structs == other.structs and
                self.enums == other.enums and
                self.type_definitions == other.type_definitions and
                self.state_variables == other.state_variables and
                self.events == other.events and
                self.custom_errors == other.custom_errors and
                self.using_directives == other.using_directives
            )
        return False