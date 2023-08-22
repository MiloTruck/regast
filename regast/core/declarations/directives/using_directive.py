from typing import List

from regast.core.core import Core
from regast.core.types.type import Type
from regast.core.types.user_defined_type import UserDefinedType
from regast.parsing.ast_node import ASTNode

class UsingDirective(Core):
    def __init__(self, node: ASTNode):
        super().__init__(node)

        self._libraries: List[UserDefinedType] = []
        self._type: Type = type
        self._any_type: bool = False
        self._global: bool = False

    @property
    def libraries(self) -> List[UserDefinedType]:
        return list(self._libraries)

    @property
    def type(self) -> Type:
        return self._type

    @property
    def any_type(self) -> bool:
        return self._any_type

    @property
    def is_global(self) -> bool:
        return self._global

    @property
    def children(self) -> List:
        return [self.type] + self.libraries

    def __eq__(self, other):
        if isinstance(other, UsingDirective):
            return self.libraries == other.libraries and self.type == other.type and self.is_global == other.is_global
        return False