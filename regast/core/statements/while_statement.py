from typing import List
from regast.core.expressions.expression import Expression
from regast.core.statements.statement import Statement
from regast.parsing.ast_node import ASTNode


class WhileStatement(Statement):
    def __init__(self, node: ASTNode):
        """
        while ( <condition> ) { <body> }
        """
        super().__init__(node)

        self._condition: Expression = None
        self._body: Statement = None

    @property
    def condition(self) -> Expression:
        return self._condition

    @property
    def body(self) -> Statement:
        return self._body

    @property
    def children(self) -> List:
        return [self.condition, self.body]

    def __eq__(self, other):
        if isinstance(other, WhileStatement):
            return self.condition == other.condition and self.body == other.body
        return False