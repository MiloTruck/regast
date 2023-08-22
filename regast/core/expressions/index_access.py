from typing import List

from regast.core.expressions.expression import Expression

class IndexAccess(Expression):
    def __init__(
        self, 
        expressions: List[Expression]
    ):
        super().__init__()

        assert len(expressions) == 2

        self._expressions: List[Expression] = expressions

    @property
    def expressions(self) -> List[Expression]:
        return list(self._expressions)

    @property
    def object(self) -> Expression:
        return self._expressions[0]

    @property
    def index(self) -> Expression:
        return self._expressions[1]
        
    @property
    def children(self) -> List:
        return self.expressions

    def __str__(self):
        return str(self.object) + "[" + str(self.index) + "]"

    def __eq__(self, other):
        if isinstance(other, IndexAccess):
            return self.expressions == other.expressions
        return False