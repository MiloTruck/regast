from regast.core.expressions.expression import Expression
from regast.core.expressions.identifier import Identifier
from regast.core.types.type import Type
from regast.core.variables.variable import Variable
from regast.parsing.ast_node import ASTNode

class Constant(Variable):
    def __str__(self):
        return str(self.type) + " constant " + str(self.name) + " = " + self.initial_expression