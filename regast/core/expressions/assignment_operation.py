from enum import Enum
from typing import List

from regast.core.expressions.expression import Expression
from regast.parsing.ast_node import ASTNode

class AssignmentOperator(str, Enum):
    ASSIGN = "="
    ASSIGN_OR = "|="
    ASSIGN_CARET = "^="
    ASSIGN_AND = "&="
    ASSIGN_LEFT_SHIFT = "<<="
    ASSIGN_RIGHT_SHIFT = ">>="
    ASSIGN_THREE_RIGHT_SHIFT = ">>>="
    ASSIGN_ADDITION = "+="
    ASSIGN_SUBTRACTION = "-="
    ASSIGN_MULTIPLICATION = "*="
    ASSIGN_DIVISION = "/="
    ASSIGN_MODULO = "%="

    def __str__(self):
        return self.value

class AssignmentOperation(Expression):
    def __init__(self, node: ASTNode):
        super().__init__(node)

        self._left_expression: Expression = None
        self._right_expression: Expression = None
        self._operator: AssignmentOperator = None

    @property
    def left_expression(self) -> Expression:
        return self._left_expression

    @property
    def right_expression(self) -> Expression:
        return self._right_expression

    @property
    def operator(self) -> AssignmentOperator:
        return self._operator

    @property
    def children(self) -> List:
        return [self.left_expression, self.right_expression]

    def __str__(self):
        return str(self.left_expression) + ' ' + str(self.operator) + ' ' + str(self.right_expression)

    def __eq__(self, other):
        if isinstance(other, AssignmentOperation):
            return (
                self.left_expression == other.left_expression and
                self.right_expression == other.right_expression and
                self.operator == other.operator
            )
        return False