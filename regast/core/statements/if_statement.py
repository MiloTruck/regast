from typing import List, Optional

from regast.core.expressions.expression import Expression
from regast.core.statements.statement import Statement
from regast.parsing.ast_node import ASTNode

class IfStatement(Statement):
    def __init__(self, node: ASTNode):
        """
        if ( <condition> ) { <true_body> } else { <false_body> }
        """
        super().__init__(node)

        self._condition: Expression = None
        self._true_body: Statement = None
        self._false_body: Optional[Statement] = None
    
    @property
    def condition(self) -> Expression:
        return self._condition

    @property
    def true_body(self) -> Statement:
        return self._true_body

    @property
    def false_body(self) -> Optional[Statement]:
        return self._false_body

    @property
    def children(self) -> List:
        children = [self.condition, self.true_body]
        if self.false_body:
            children.append(self.false_body)
        return children

    def __eq__(self, other):
        if isinstance(other, IfStatement):
            return self.condition == other.condition and self.true_body == other.true_body and self.false_body == other.false_body
        return False