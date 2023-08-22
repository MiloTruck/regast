from typing import List, Optional

from regast.core.expressions.expression import Expression
from regast.core.statements.statement import Statement
from regast.core.statements.variable_declaration_statement import VariableDeclarationStatement
from regast.parsing.ast_node import ASTNode


class ForStatement(Statement):
    def __init__(self, node: ASTNode):
        """
        for ( <initialization> ; <condition> ; <iteration> ) { <body> }
        """
        super().__init__(node)

        self._body: Statement = None
        self._initialization: Optional[VariableDeclarationStatement] = None
        self._condition: Optional[Expression] = None
        self._iteration: Optional[Expression] = None

    @property
    def body(self) -> Statement:
        return self._body

    @property
    def initialization(self) -> Optional[VariableDeclarationStatement]:
        return self._initialization

    @property
    def condition(self) -> Optional[Expression]:
        return self._condition

    @property
    def iteration(self) -> Optional[Expression]:
        return self._iteration

    @property
    def children(self) -> List:
        return [self.body] + [x for x in [self.initialization, self.condition, self.iteration] if x]

    def __eq__(self, other):
        if isinstance(other, ForStatement):
            return self.body == other.body and self.initialization == other.initialization and self.condition == other.condition and self.iteration == other.iteration
        return False