from typing import List, Optional

from regast.core.expressions.expression import Expression
from regast.parsing.ast_node import ASTNode

class ArrayAccess(Expression):
    def __init__(self, node: ASTNode):
        super().__init__(node)

        self._object: Expression = None
        self._index: Optional[Expression] = None

    @property
    def object(self) -> Expression:
        return self._object
    
    @property
    def index(self) -> Optional[Expression]:
        return self._index

    @property
    def children(self) -> List:
        return [self.object] + ([self.index] if self.index else [])

    def __str__(self):
        index_str = str(self.index) if self.index else ''
        return str(self.object) + "[" + index_str + "]"
    
    def __eq__(self, other):
        if isinstance(other, ArrayAccess):
            return self.object == other.object and self.index == other.index
        return False
