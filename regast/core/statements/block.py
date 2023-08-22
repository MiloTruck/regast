from typing import List

from regast.core.statements.statement import Statement
from regast.parsing.ast_node import ASTNode

class Block(Statement):
    def __init__(self, node: ASTNode):
        super().__init__(node)

        self._statements: List[Statement] = []
        self._unchecked: bool = False
    
    @property
    def statements(self) -> List[Statement]:
        return list(self._statements)

    @property
    def is_unchecked(self) -> bool:
        return self._unchecked

    @property
    def children(self) -> List:
        return self.statements

    def __eq__(self, other):
        if isinstance(other, Block):
            return self.statements == other.statements
        return False