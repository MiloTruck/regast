from typing import List, Optional

from regast.core.expressions.expression import Expression
from regast.core.statements.statement import Statement
from regast.parsing.ast_node import ASTNode

class ReturnStatement(Statement):
    def __init__(self, node: ASTNode):
        super().__init__(node)

        self._return_value: Optional[Expression] = None

    @property
    def return_value(self) -> Optional[Expression]:
        return self._return_value

    @property
    def children(self) -> List:
        return [self.return_value] if self.return_value else []

    def __eq__(self, other):
        if isinstance(other, ReturnStatement):
            return self.return_value == other.return_value
        return False
            