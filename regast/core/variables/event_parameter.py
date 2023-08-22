from regast.core.variables.variable import Variable
from regast.parsing.ast_node import ASTNode

class EventParameter(Variable):
    def __init__(self, node: ASTNode):
        super().__init__(node)

        self._indexed: bool = False

    @property
    def is_indexed(self) -> bool:
        return self._indexed

    def __str__(self):
        s = str(self.type)
        if self.is_indexed:
            s += " indexed"
        if self.name:
            s += " " + str(self.name)
        return s
        
    def __eq__(self, other):
        if isinstance(other, EventParameter):
            return self.type == other.type and self.is_indexed == other.is_indexed and self.name == other.name
        return False