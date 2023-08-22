from enum import Enum
from typing import List

from regast.core.expressions.expression import Expression
from regast.parsing.ast_node import ASTNode

class UpdateOperator(str, Enum):
    PLUSPLUS = '++'
    MINUSMINUS = '--'

    def __str__(self):
        return self.value

class UpdateOperation(Expression):
    def __init__(self, node: ASTNode):
        super().__init__(node)

        self._expression: Expression = None
        self._operator: UpdateOperator = None
        self._prefix: bool = False
        
    @property
    def expression(self) -> Expression:
        return self._expression
    
    @property
    def operator(self) -> UpdateOperator:
        return self._operator

    @property
    def is_prefix(self) -> bool:
        return self._prefix
    
    @property
    def children(self) -> List:
        return [self.expression]

    def __str__(self):
        if self.is_prefix:
            return str(self.operator) + str(self.expression)
        return str(self.expression) + str(self.operator)

    def __eq__(self, other):
        if isinstance(other, UpdateOperation):
            return (
                self.expression == other.expression and 
                self.operator == other.operator and
                self.is_prefix == other.is_prefix
            )
        return False