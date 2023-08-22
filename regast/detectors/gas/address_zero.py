from typing import List

from regast.core.expressions.binary_operation import BinaryOperation
from regast.core.expressions.literal import Literal
from regast.core.expressions.type_cast_expression import TypeCastExpression
from regast.core.types.elementary_type import ElementaryType
from regast.detectors.detector import Detector, DetectorClassification
from regast.detectors.result import Result


class AddressZero(Detector):
    NAME = 'Use assembly to check for `address(0)`'
    CLASSIFICATION = DetectorClassification.GAS
    DESCRIPTION = "*Saves 6 gas per instance*"

    def detect(self) -> List[Result]:
        # Checks if an expression matches address(0)
        def is_address_zero(expression):
            return (
                isinstance(expression, TypeCastExpression) and
                isinstance(literal := expression.casted_expression, Literal) and
                literal.value == 0 and
                isinstance(casted_type := expression.type, ElementaryType) and
                str(casted_type) == 'address'
            )

        # Checks if a binary operation is a comparison to address(0)
        # (Has '==" or "!=" operator and has address(0) on either side)
        def is_compare_to_address_zero(binary_operation):
            return str(binary_operation.operator) in ['==', '!='] and (
                is_address_zero(binary_operation.left_expression) or 
                is_address_zero(binary_operation.right_expression)
            )
        
        results = []

        for source_unit in self.source_units:
            binary_operations = source_unit.get_instances_of(BinaryOperation)
            binary_operations = filter(is_compare_to_address_zero, binary_operations)
            results.extend(binary_operations)

        return self.generate_results_from_core_objects(results)