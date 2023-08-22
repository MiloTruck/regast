from typing import List

from regast.core.expressions.literal import Literal
from regast.core.expressions.type_cast_expression import TypeCastExpression
from regast.core.statements.variable_declaration_statement import VariableDeclarationStatement
from regast.core.types.elementary_type import ElementaryType
from regast.detectors.detector import Detector, DetectorClassification
from regast.detectors.result import Result


class InitializeDefaultValue(Detector):
    NAME = 'Unnecessary initialization of variables with default values' 
    CLASSIFICATION = DetectorClassification.GAS
    DESCRIPTION = "Don't initialize variables with default value"

    def detect(self) -> List[Result]:
        # Check if an expression matches address(0), taken from the AddressZero detector
        # https://github.com/MiloTruck/regast/blob/main/regast/detectors/gas/address_zero.py
        def is_address_zero(expression):
            return (
                isinstance(expression, TypeCastExpression) and
                isinstance(literal := expression.casted_expression, Literal) and
                literal.value == 0 and
                isinstance(casted_type := expression.type, ElementaryType) and
                str(casted_type) == 'address'
            )

        # Check if variable declaration is either:
        """
        bool ... = false
        uint/int ... = 0
        address ... = 0 or address(0)
        """
        def initialized_with_default_value(variable):
            if isinstance(elementary_type := variable.type, ElementaryType):
                if isinstance(literal := variable.initial_expression, Literal):
                    return (
                        str(elementary_type) == 'bool' and literal.value == False or
                        (str(elementary_type) == 'address' or 'int' in str(elementary_type)) and
                        literal.value == 0
                    )
                else:
                    return str(elementary_type) == 'address' and is_address_zero(variable.initial_expression)
            
            return False

        results = []

        for source_unit in self.source_units:
            for contract in source_unit.all_contracts:
                # Get all definitions of local variables
                variable_declaration_statements = contract.get_instances_of(VariableDeclarationStatement)

                # Check state and local variables for default values
                variables_with_default_value = filter(
                    initialized_with_default_value,
                    contract.state_variables + variable_declaration_statements
                )

                results.extend(variables_with_default_value)

        return self.generate_results_from_core_objects(results)