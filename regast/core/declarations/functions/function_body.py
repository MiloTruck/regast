from typing import List, Optional

from regast.core.core import Core
from regast.core.statements.block import Block
from regast.core.statements.variable_declaration_statement import VariableDeclarationFromTupleStatement, VariableDeclarationStatement
from regast.core.variables.local_variable import LocalVariable
from regast.parsing.ast_node import ASTNode


class FunctionBody(Core):
    def __init__(self, node: ASTNode):
        super().__init__(node)

        self._body: Optional[Block] = None
        self._local_variables: List[LocalVariable] = []

    @property
    def body(self) -> Optional[Block]:
        return self._body

    @property
    def local_variables(self) -> List[LocalVariable]:
        # Function to recursively find local variables
        def find_variable_declarations(block: Block):
            for statement in block.statements:
                if isinstance(statement, Block):
                    find_variable_declarations(statement)
                
                elif isinstance(statement, VariableDeclarationStatement):
                    self._local_variables.append(statement.local_variable)

                elif isinstance(statement, VariableDeclarationFromTupleStatement):
                    self._local_variables.extend(statement.local_variables)

        if not self._local_variables:
            find_variable_declarations(self.body)
        return list(self._local_variables)
