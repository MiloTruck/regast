from enum import Enum
from typing import List

from regast.core.expressions.expression import Expression
from regast.parsing.ast_node import ASTNode

class UnaryOperator(str, Enum):
    BANG = '!'
    TILDE = '~'
    DELETE = 'delete'
    AFTER = 'after'
    PLUS = '+'
    MINUS = '-'

    def __str__(self):
        return self.value

class UnaryOperation(Expression):
    def __init__(self, node: ASTNode):
        super().__init__(node)

        self._expression: Expression = None
        self._operator: UnaryOperator = None
        
    @property
    def expression(self) -> Expression:
        return self._expression
    
    @property
    def operator(self) -> UnaryOperator:
        return self._operator
    
    @property
    def children(self) -> List:
        return [self.expression]

    def __str__(self):
        if self.operator in [UnaryOperator.DELETE, UnaryOperator.AFTER]:
            return str(self.operator) + ' ' + str(self.expression)
        return str(self.operator) + str(self.expression)

    def __eq__(self, other):
        if isinstance(other, UnaryOperation):
            return self.expression == other.expression and self.operator == other.operator
        return False