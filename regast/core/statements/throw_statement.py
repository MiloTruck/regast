from regast.core.statements.statement import Statement

class ThrowStatement(Statement):
    def __eq__(self, other):
        if isinstance(other, str):
            return other == "throw"
        return isinstance(other, ThrowStatement)