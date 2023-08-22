from typing import List, Optional

from regast.core.expressions.expression import Expression
from regast.core.expressions.struct_expression import StructArguments
from regast.core.statements.statement import Statement
from regast.parsing.ast_node import ASTNode


class EmitStatement(Statement):
    def __init__(self, node: ASTNode):
        super().__init__(node)

        self._event_name: Expression = None
        self._struct_arguments: Optional[StructArguments] = None
        self._arguments: List[Expression] = []

    @property
    def event_name(self) -> Expression:
        return self._event_name

    @property
    def struct_arguments(self) -> Optional[StructArguments]:
        return self._struct_arguments

    @property
    def arguments(self) -> List[Expression]:
        return list(self._arguments)

    @property
    def children(self) -> List:
        children = [self.event_name] + self.arguments
        if self.struct_arguments:
            children.append(self.struct_arguments)
        return children

    def __eq__(self, other):
        if isinstance(other, EmitStatement):
            return (
                self.event_name == other.event_name and
                self.struct_arguments == other.struct_arguments and
                self.arguments == other.arguments
            )
        return False