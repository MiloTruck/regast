from typing import List, Optional

from regast.core.core import Core
from regast.core.expressions.expression import Expression
from regast.core.expressions.identifier import Identifier
from regast.core.statements.statement import Statement
from regast.core.statements.block import Block
from regast.core.variables.parameter import Parameter
from regast.parsing.ast_node import ASTNode

class CatchClause(Core):
    def __init__(self, node: ASTNode):
        super().__init__(node)

        self._body: Block = None
        self._parameters: List[Parameter] = []
        self._error: Optional[Identifier] = None

    @property
    def body(self) -> Block:
        return self._body
    
    @property
    def parameters(self) -> List[Parameter]:
        return list(self._parameters)

    @property
    def error(self) -> Optional[Identifier]:
        return self._error

    @property
    def children(self) -> List:
        children = [self.body] + self.parameters
        if self.error:
            children.append(self.error)
        return children

    def __eq__(self, other):
        if isinstance(other, CatchClause):
            return self.body == other.body and self.parameters == other.parameters and self.error == other.error
        return False

class TryStatement(Statement):
    def __init__(self, node: ASTNode):
        super().__init__(node)

        self._try_expression: Expression = None
        self._body: Block = None
        self._catch_clauses: List[CatchClause] = []
        self._parameters: List[Parameter] = []

    @property
    def try_expression(self) -> Expression:
        return self._try_expression

    @property
    def body(self) -> Block:
        return self._body

    @property
    def catch_clauses(self) -> List[CatchClause]:
        return list(self._catch_clauses)

    @property
    def parameters(self) -> List[Parameter]:
        return list(self._parameters)

    @property
    def children(self) -> List:
        return [self.try_expression, self.body] + self.catch_clauses + self.parameters

    def __eq__(self, other):
        if isinstance(other, TryStatement):
            return self.try_expression == other.try_expression and self.body == other.body and self.catch_clauses == other.catch_clauses and self.parameters == other.parameters
        return False

