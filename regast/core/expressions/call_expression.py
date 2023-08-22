from typing import List, Optional
from regast.core.expressions.expression import Expression
from regast.core.expressions.struct_expression import StructArguments
from regast.parsing.ast_node import ASTNode

class CallExpression(Expression):
    def __init__(self, node: ASTNode):
        super().__init__(node)
    
        self._function_name: Expression = None
        self._struct_arguments: Optional[StructArguments] = None
        self._arguments: List[Expression] = []

    @property
    def function_name(self) -> Expression:
        return self._function_name

    @property
    def struct_arguments(self) -> Optional[StructArguments]:
        return self._struct_arguments

    @property
    def arguments(self) -> List[Expression]:
        return list(self._arguments)

    @property
    def gas(self) -> Optional[Expression]:
        if self.struct_arguments and "gas" in self.struct_arguments.fields:
            return self.struct_arguments.get_argument_by_field("gas")

    @property
    def value(self) -> Optional[Expression]:
        if self.struct_arguments and "value" in self.struct_arguments.fields:
            return self.struct_arguments.get_argument_by_field("value")

    @property
    def salt(self) -> Optional[Expression]:
        if self.struct_arguments and "salt" in self.struct_arguments.fields:
            return self.struct_arguments.get_argument_by_field("salt")

    @property
    def children(self) -> List:
        children = [self.function_name] + self.arguments
        if self.struct_arguments:
            children.append(self.struct_arguments)
        return children

    def __str__(self):
        s = str(self.function_name)
        if self.struct_arguments:
            s += str(self.struct_arguments)
        s += "(" + ", ".join([str(x) for x in self.arguments]) + ")"
        return s

    def __eq__(self, other):
        if isinstance(other, CallExpression):
            return (
                self.function_name == other.function_name and 
                self.struct_arguments == other.struct_arguments and 
                self.arguments == other.arguments 
            )
        return False
            