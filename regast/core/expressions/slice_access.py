from typing import List, Optional

from regast.core.expressions.expression import Expression
from regast.parsing.ast_node import ASTNode

class SliceAccess(Expression):
    def __init__(self, node: ASTNode):
        super().__init__(node)

        self._object: Expression = None
        self._start: Optional[Expression] = None
        self._stop: Optional[Expression] = None

    @property
    def object(self) -> Expression:
        return self._object
    
    @property
    def start(self) -> Optional[Expression]:
        return self._start

    @property
    def stop(self) -> Optional[Expression]:
        return self._stop

    @property
    def children(self) -> List:
        return [self.object] + [x for x in [self.start, self.stop] if x] 

    def __str__(self):
        start = str(self.start) if self.start else ""
        stop = str(self.stop) if self.stop else ""
        return str(self.object) + "[" + start + ":" + stop + "]"
    
    def __eq__(self, other):
        if isinstance(other, SliceAccess):
            return self.object == other.object and self.start == other.start and self.stop == other.stop
        return False
