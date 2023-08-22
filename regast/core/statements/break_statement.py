from regast.core.statements.statement import Statement

class BreakStatement(Statement):
    def __eq__(self, other):
        if isinstance(other, str):
            return other == "break"
        return isinstance(other, BreakStatement)
            