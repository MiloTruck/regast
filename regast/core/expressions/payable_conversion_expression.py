from typing import List, Optional
from regast.core.expressions.expression import Expression
from regast.core.expressions.struct_expression import StructArguments
from regast.parsing.ast_node import ASTNode

class PayableConversionExpression(Expression):
    def __init__(self, node: ASTNode):
        super().__init__(node)
    
        self._struct_arguments: Optional[StructArguments] = None
        self._arguments: List[Expression] = []

    @property
    def struct_arguments(self) -> Optional[StructArguments]:
        return self._struct_arguments

    @property
    def arguments(self) -> List[Expression]:
        return list(self._arguments)

    @property
    def children(self) -> List:
        return self.arguments + ([self.struct_arguments] if self.struct_arguments else [])

    def __str__(self):
        s = 'payable'
        if self.struct_arguments:
            s += str(self.struct_arguments)
        s += "(" + ", ".join([str(x) for x in self.arguments]) + ")"
        return s

    def __eq__(self, other):
        if isinstance(other, PayableConversionExpression):
            return (
                self.struct_arguments == other.struct_arguments and 
                self.arguments == other.arguments 
            )
        return False
            