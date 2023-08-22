from regast.core.statements.statement import Statement

class ContinueStatement(Statement):
    def __eq__(self, other):
        if isinstance(other, str):
            return other == "continue"
        return isinstance(other, ContinueStatement)
            