from typing import List

from regast.core.core import Core
from regast.core.declarations.contracts.contract import Contract
from regast.core.declarations.contracts.interface import Interface
from regast.core.declarations.contracts.library import Library
from regast.core.declarations.custom_error import CustomError
from regast.core.declarations.directives.using_directive import UsingDirective
from regast.core.declarations.enum import Enum
from regast.core.declarations.functions.function import Function
from regast.core.declarations.directives.import_directive import Import
from regast.core.declarations.directives.pragma_directive import Pragma
from regast.core.declarations.struct import Struct
from regast.core.declarations.type_definition import TypeDefinition
from regast.core.others.comment import Comment
from regast.core.variables.constant import Constant
from regast.parsing.ast_node import ASTNode

class SourceUnit(Core):
    def __init__(self, node: ASTNode, fname: str):
        super().__init__(node)

        self._fname: str = fname

        self._comments: List[Comment] = []

        self._pragma_directives: List[Pragma] = []
        self._import_directives: List[Import] = []
        self._using_directives: List[UsingDirective] = []
        
        self._contracts: List[Contract] = []
        self._interfaces: List[Interface] = []
        self._libraries: List[Library] = []
        
        self._enums: List[Enum] = []
        self._structs: List[Struct] = []
        self._functions: List[Function] = []
        self._constants: List[Constant] = []
        self._custom_errors: List[CustomError] = []
        self._type_definitions: List[TypeDefinition ] = []

    @property
    def fname(self) -> str:
        return self._fname
    
    @property
    def comments(self) -> List[Comment]:
        return list(self._comments)

    @property
    def pragma_directives(self) -> List[Pragma]:
        return list(self._pragma_directives)

    @property
    def using_directives(self) -> List[UsingDirective]:
        return list(self._using_directives)

    @property
    def import_directives(self) -> List[Import]:
        return list(self._import_directives)

    @property
    def contracts(self) -> List[Contract]:
        return list(self._contracts)
        
    @property
    def interfaces(self) -> List[Interface]:
        return list(self._interfaces)
        
    @property
    def libraries(self) -> List[Library]:
        return list(self._libraries)
    
    @property
    def all_contracts(self) -> List[Contract]:
        """
        All contracts, inclusive of interfaces and libraries
        """
        return self.contracts + self.interfaces + self.libraries

    @property
    def enums(self) -> List[Enum]:
        return list(self._enums)

    @property
    def structs(self) -> List[Struct]:
        return list(self._structs)

    @property
    def functions(self) -> List[Function]:
        return list(self._functions)

    @property
    def constants(self) -> List[Constant]:
        return list(self._constants)

    @property
    def custom_errors(self) -> List[CustomError]:
        return list(self._custom_errors)

    @property
    def type_definitions(self) -> List[TypeDefinition]:
        return list(self._type_definitions)

    @property
    def children(self) -> List:
        children = self.pragma_directives
        children += self.import_directives
        children += self.using_directives
        children += self.all_contracts
        children += self.enums
        children += self.structs
        children += self.functions
        children += self.constants
        children += self.custom_errors
        children += self.type_definitions
        return children

    def __eq__(self, other):
        if isinstance(other, SourceUnit):
            return (
                self.pragma_directives == other.pragma_directives and
                self.import_directives == other.import_directives and
                self.using_directives == other.using_directives and
                self.all_contracts == other.all_contracts and
                self.enums == other.enums and
                self.structs == other.structs and
                self.functions == other.functions and
                self.constants == other.constants and
                self.custom_errors == other.custom_errors and
                self.type_definitions == other.type_definitions
            )
        return False