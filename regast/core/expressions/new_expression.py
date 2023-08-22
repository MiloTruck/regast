from typing import List
from regast.core.expressions.expression import Expression
from regast.core.types.type import Type
from regast.parsing.ast_node import ASTNode

class NewExpression(Expression):
    def __init__(self, node: ASTNode):
        super().__init__(node)

        self._type = None

    @property
    def type(self) -> Type:
        return self._type

    @property
    def children(self) -> List:
        return [self.type]

    def __str__(self):
        return "new " + str(self.type)
    
    def __eq__(self, other):
        if isinstance(other, NewExpression):
            return self.type == other.type
        return False
