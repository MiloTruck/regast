from typing import Dict, List, Optional, Union
from regast.core.core import Core

from regast.core.declarations.contracts.contract import Contract
from regast.core.declarations.functions.function import Function
from regast.core.declarations.source_unit import SourceUnit
from regast.core.expressions.identifier import Identifier
from regast.core.statements.block import Block
from regast.core.statements.do_while_statement import DoWhileStatement
from regast.core.statements.for_statement import ForStatement
from regast.core.statements.variable_declaration_statement import VariableDeclarationFromTupleStatement, VariableDeclarationStatement
from regast.core.statements.while_statement import WhileStatement
from regast.core.variables.variable import Variable
from regast.exceptions import RegastException


class Scope:
    def __init__(self):
        self._contracts: Dict[Identifier, Contract] = {}
        self._functions: Dict[Identifier, Function] = {}
        self._variables: Dict[Identifier, Variable] = {}

    def add_contracts(self, contracts: List[Contract]):
        for contract in contracts:
            assert contract.name not in self._contracts
            self._contracts[contract.name] = contract

    def add_functions(self, functions: List[Function]):
        for function in functions:
            assert function.name and function.name not in self._functions
            self._functions[function.name] = function

    def add_variable(self, variable: List[Variable]):
        assert variable.name not in self._variables
        self._variables[variable.name] = variable

    def add_variables(self, variables: List[Variable]):
        for variable in variables:
            self.add_variable(variable)

    def get_contract_by_name(self, name: Identifier) -> Optional[Contract]:
        if name in self._contracts:
            return self._contracts[name]

    def get_function_by_name(self, name: Identifier) -> Optional[Function]:
        if name in self._functions:
            return self._functions[name]

    def get_variable_by_name(self, name: Identifier) -> Optional[Variable]:
        if name in self._variables:
            return self._variables[name]

class NameResolver:
    def __init__(self):
        self._source_units: List[SourceUnit] = []

    def add_source_unit(self, source_unit: SourceUnit):
        self._source_units.append(source_unit)

    def resolve_names(self):
        # Recursive function to create a new scope for each object and resolve names
        def resolve(scope_stack: List[Scope], core_object: Core):
            scope = Scope()
            child_core_objects = []

            if isinstance(core_object, SourceUnit):
                scope.add_contracts(core_object.all_contracts)
                scope.add_functions(core_object.functions)
                scope.add_variables(core_object.constants)

                child_core_objects = core_object.all_contracts + core_object.functions

            elif isinstance(core_object, Contract):
                scope.add_functions(core_object.functions)
                scope.add_variables(core_object.state_variables)

                child_core_objects = core_object.all_functions

            elif isinstance(core_object, Function):
                named_parameters = [p for p in core_object.parameters + core_object.return_parameters if p.name]
                scope.add_variables(named_parameters)

                if core_object.body:
                    child_core_objects.append(core_object.body)

            elif isinstance(core_object, WhileStatement) or isinstance(core_object, DoWhileStatement):
                pass

            elif isinstance(core_object, ForStatement):
                if core_object.initialization:
                    scope.add_variables(core_object.initialization)


            # Block is where name resolution occurs
            elif isinstance(core_object, Block):
                for statement in core_object.statements:
                    # Perform name resolution on nested Blocks
                    if isinstance(statement, Block):
                        child_core_objects.append(statement)

                    # Add new variables to scope for variable declaration statements
                    elif isinstance(statement, VariableDeclarationStatement):
                        scope.add_variable(statement.local_variable)

                    elif isinstance(statement, VariableDeclarationFromTupleStatement):
                        scope.add_variables(statement.local_variables)

                    else:
                        pass
            
            # core_object is of an unknown type
            else:
                raise RegastException(f'Unknown core type for name resolution: {core_object.__class__.__name__}')

            # Perform name resolution on all child core objects
            for child_core_object in child_core_objects:
                resolve(scope_stack + [scope], child_core_object)

        # Perform name resolution on each source unit, starting with an empty scope stack
        # Note: Perform import resolution here and start with a non-empty scope stack below
        for source_unit in self._source_units:
            resolve([], source_unit)

            