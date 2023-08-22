from typing import List
from regast.core.expressions.expression import Expression
from regast.parsing.ast_node import ASTNode

class ParenthesizedExpression(Expression):
    def __init__(self, node: ASTNode):
        super().__init__(node)
    
        self._expression: Expression = None

    @property
    def expression(self) -> Expression:
        return self._expression

    @property
    def children(self) -> List:
        return [self.expression]

    def __str__(self):
        return '(' + str(self.expression) + ')'

    def __eq__(self, other):
        if isinstance(other, ParenthesizedExpression):
            return self.expression == other.expression
        return False
            