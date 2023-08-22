from enum import Enum
from typing import List

from regast.core.expressions.expression import Expression
from regast.parsing.ast_node import ASTNode

class BinaryOperator(str, Enum):
    POWER = "**"
    MULTIPLICATION = "*"
    DIVISION = "/"
    MODULO = "%"
    ADDITION = "+"
    SUBTRACTION = "-"
    LEFT_SHIFT = "<<"
    RIGHT_SHIFT = ">>"
    THREE_RIGHT_SHIFT = ">>>"
    AND = "&"
    CARET = "^"
    OR = "|"
    LESS = "<"
    GREATER = ">"
    LESS_EQUAL = "<="
    GREATER_EQUAL = ">="
    EQUAL = "=="
    NOT_EQUAL = "!="
    ANDAND = "&&"
    OROR = "||"

    def __str__(self):
        return self.value

class BinaryOperation(Expression):
    def __init__(self, node: ASTNode):
        super().__init__(node)

        self._left_expression: Expression = None
        self._right_expression: Expression = None
        self._operator: BinaryOperation = None

    @property
    def left_expression(self) -> Expression:
        return self._left_expression

    @property
    def right_expression(self) -> Expression:
        return self._right_expression

    @property
    def operator(self) -> BinaryOperator:
        return self._operator
        
    @property
    def children(self) -> List:
        return [self.left_expression, self.right_expression]

    def __str__(self):
        return f'{self.left_expression} {self.operator} {self.right_expression}'

    def __eq__(self, other):
        if isinstance(other, BinaryOperation):
            return (
                self.left_expression == other.left_expression and
                self.right_expression == other.right_expression and
                self.operator == other.operator
            )
        return False