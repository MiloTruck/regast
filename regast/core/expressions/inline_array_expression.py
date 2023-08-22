from typing import List

from regast.core.expressions.expression import Expression
from regast.parsing.ast_node import ASTNode

class InlineArrayExpression(Expression):
    def __init__(self, node: ASTNode):
        super().__init__(node)

        self._expressions: List[Expression] = []

    @property
    def expressions(self) -> List[Expression]:
        return list(self._expressions)

    @property
    def children(self) -> List:
        return self.expressions

    def __str__(self):
        return "[" + ", ".join([str(x) for x in self.expressions]) + "]"
    
    def __eq__(self, other):
        if isinstance(other, InlineArrayExpression):
            return self.expressions == other.expressions
        return False
