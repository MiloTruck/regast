from typing import List
from regast.core.expressions.expression import Expression
from regast.core.types.elementary_type import ElementaryType
from regast.parsing.ast_node import ASTNode

class TypeCastExpression(Expression):
    def __init__(self, node: ASTNode):
        super().__init__(node)

        self._type: ElementaryType = None
        self._expression: Expression = None

    @property
    def type(self) -> ElementaryType:
        return self._type

    @property
    def casted_expression(self) -> Expression:
        return self._expression
    
    @property
    def children(self) -> List:
        return [self.type, self.casted_expression]

    def __str__(self):
        return str(self.type) + "(" + str(self.casted_expression) + ")"

    def __eq__(self, other):
        if isinstance(other, TypeCastExpression):
            return self.type == other.type and self.casted_expression == other.casted_expression
        return False

