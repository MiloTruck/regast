from typing import List, Optional

from regast.core.expressions.expression import Expression
from regast.core.expressions.identifier import Identifier
from regast.core.statements.statement import Statement
from regast.core.types.type import Type
from regast.core.variables.local_variable import LocalVariable
from regast.core.variables.variable import DataLocation
from regast.parsing.ast_node import ASTNode

class VariableDeclarationStatement(Statement):
    def __init__(self, local_variable: LocalVariable):
        super().__init__(local_variable.ast_node)

        self._local_variable: LocalVariable = local_variable

    @property
    def local_variable(self) -> LocalVariable:
        return self._local_variable

    @property
    def type(self) -> Type:
        return self.local_variable.type

    @property
    def name(self) -> Identifier:
        return self.local_variable.name

    @property
    def data_location(self) -> Optional[DataLocation]:
        return self.local_variable.data_location

    @property
    def initial_expression(self) -> Optional[Expression]:
        return self.local_variable.initial_expression

    @property
    def children(self) -> List:
        children = [self.type, self.name]
        if self.initial_expression:
            children.append(self.initial_expression)
        return children

    def __eq__(self, other):
        if isinstance(other, VariableDeclarationStatement):
            return self.local_variable == other.local_variable
        return False

class VariableDeclarationFromTupleStatement(Statement):
    def __init__(self, local_variables: List[LocalVariable]):
        assert local_variables

        super().__init__(local_variables[0].ast_node)

        self._local_variables: List[LocalVariable] = local_variables
        
    @property
    def local_variables(self) -> List[LocalVariable]:
        return list(self._local_variables)

    @property
    def types(self) -> List[Type]:
        return [lv.type for lv in self.local_variables]

    @property
    def names(self) -> List[Identifier]:
        return [lv.name for lv in self.local_variables]

    @property
    def data_locations(self) -> List[Optional[DataLocation]]:
        return [lv.data_location for lv in self.local_variables]

    @property
    def initial_expression(self) -> Expression:
        return self.local_variables[0].initial_expression

    @property
    def children(self) -> List:
        children = self.types + self.names
        if self.initial_expression:
            children.append(self.initial_expression)
        return children
        
    def __eq__(self, other):
        if isinstance(other, VariableDeclarationFromTupleStatement):
            return self.local_variables == other.local_variables
        return False

class VariableDeclarationWithVarStatement(Statement):
    def __init__(self, node: ASTNode):
        """
        Deprecated since v0.4.20
        var (x, y, z) = f()
        """
        super().__init__(node)

        self._names: List[Identifier] = []
        self._expression: Expression = None

    @property
    def names(self) -> List[Identifier]:
        return self._names

    @property
    def initial_expression(self) -> Expression:
        return self._expression

    @property
    def children(self) -> List:
        return self.names + [self.initial_expression]

    def __eq__(self, other):
        if isinstance(other, VariableDeclarationWithVarStatement):
            return self.names == other.names and self.initial_expression == other.initial_expression
        return False