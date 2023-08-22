from typing import List

from regast.core.expressions.binary_operation import BinaryOperation
from regast.core.expressions.literal import Literal, LiteralType
from regast.detectors.detector import Detector, DetectorClassification
from regast.detectors.result import Result


class BoolComparison(Detector):
    NAME = 'Don\'t compare booleans to `true` or `false`' 
    CLASSIFICATION = DetectorClassification.GAS
    DESCRIPTION = "`true` and `false` are constants and it is more expensive comparing a boolean against them than directly checking the returned boolean value."

    def detect(self) -> List[Result]:
        # Check if an expression is either true or false
        def is_boolean(literal):
            return isinstance(literal, Literal) and literal.type == LiteralType.BOOLEAN
        
        # Check if binary operation is a comparison to a true or false
        def is_comparison_to_boolean(binary_operation):
            return binary_operation.operator in ['==', '!='] and (
                is_boolean(binary_operation.left_expression) or
                is_boolean(binary_operation.right_expression)
            )

        results = []

        for source_unit in self.source_units:
            binary_operations = source_unit.get_instances_of(BinaryOperation)
            binary_operations = filter(is_comparison_to_boolean, binary_operations)

            results.extend(binary_operations)

        return self.generate_results_from_core_objects(results)