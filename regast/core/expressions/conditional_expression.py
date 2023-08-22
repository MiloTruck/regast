from typing import List

from regast.core.expressions.expression import Expression
from regast.parsing.ast_node import ASTNode

class ConditionalExpression(Expression):
    def __init__(self, node: ASTNode):
        """
        <condition> ? <true_expression> : <false_expression>
        """
        super().__init__(node)

        self._condition: Expression = None
        self._true_expression: Expression = None
        self._false_expression: Expression = None
    
    @property
    def condition(self) -> Expression:
        return self._condition

    @property
    def true_expression(self) -> Expression:
        return self._true_expression

    @property
    def false_expression(self) -> Expression:
        return self._false_expression

    @property
    def children(self) -> List:
        return [self.condition, self.true_expression, self.false_expression]

    def __str__(self):
        return f'{self.condition} ? {self.true_expression} : {self.false_expression}'

    def __eq__(self, other):
        if isinstance(other, ConditionalExpression):
            return (
                self.condition == other.condition and 
                self.true_expression == other.true_expression and 
                self.false_expression == other.false_expression
            )
        return False