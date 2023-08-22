from regast.core.expressions.expression import Expression
from regast.parsing.ast_node import ASTNode

class Identifier(Expression):
    @property
    def text(self):
        return self.ast_node.text

    def __hash__(self):
        return hash(self.text)

    def __str__(self):
        return self.text

    def __eq__(self, other):
        if isinstance(other, str):
            return self.text == other
        elif isinstance(other, Identifier):
            return self.text == other.text
        return False