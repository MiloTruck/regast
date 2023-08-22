from typing import Dict, List, Optional, Union

from regast.core.expressions.expression import Expression
from regast.core.expressions.identifier import Identifier
from regast.parsing.ast_node import ASTNode

class StructArguments(Expression):
    def __init__(self, node: ASTNode):
        super().__init__(node)

        self._field_to_argument: Dict[Identifier, Expression] = {}
    
    @property
    def fields(self) -> List[Expression]:
        return list(self._field_to_argument.keys())

    @property
    def arguments(self) -> List[Expression]:
        return list(self._field_to_argument.values())
    
    def get_argument_by_field(self, field: Union[Identifier, str]) -> Optional[Expression]:
        if field in self._field_to_argument:
            return self._field_to_argument[field]

    @property
    def children(self) -> List:
        return self.fields + self.arguments

    def __str__(self):
        return "{" + ", ".join([str(f) + ": " + str(a) for f, a in self._field_to_argument.items()]) + "}"

    def __eq__(self, other):
        if isinstance(other, StructArguments):
            return self._field_to_argument == other._field_to_argument
        return False


class StructExpression(Expression):
    def __init__(self, node: ASTNode):
        super().__init__(node)
    
        self._struct_name: Expression = None
        self._struct_arguments: StructArguments = StructArguments(node)

        # Not sure if this is good practice...
        self.fields = self._struct_arguments.fields
        self.arguments = self._struct_arguments.arguments
        self.get_argument_by_field = self._struct_arguments.get_argument_by_field

    @property
    def struct_name(self) -> Expression:
        return self._struct_name

    @property
    def children(self) -> List:
        return [self.struct_name] + self._struct_arguments.children

    def __str__(self):
        return str(self.struct_name) + str(self._struct_arguments)

    def __eq__(self, other):
        if isinstance(other, StructExpression):
            return self.struct_name == other.struct_name and self.fields == other.fields and self.arguments == other.arguments
        return False
            