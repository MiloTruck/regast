from typing import List

from regast.core.expressions.binary_operation import BinaryOperation
from regast.core.expressions.literal import Literal, LiteralType
from regast.detectors.detector import Detector, DetectorClassification
from regast.detectors.result import Result


class UnsignedComparison(Detector):
    NAME = 'Use `!= 0` instead of `> 0` for unsigned integer comparison'
    CLASSIFICATION = DetectorClassification.GAS

    def detect(self) -> List[Result]:
        # Checks if an expression is the number 0
        def is_zero(expression):
            return (
                isinstance(expression, Literal) and 
                expression.type in [LiteralType.NUMBER, LiteralType.HEX_STRING] and
                expression.value == 0
            )
        
        # Checks if binary operation is either ... > 0 or 0 < ...
        # Note: This function can be improved by ensuring the expression being
        # compared to 0 is actually an unsigned integer
        def is_more_than_zero_comparison(binary_operation):
            return (
                binary_operation.operator == '>' and 
                is_zero(binary_operation.right_expression) or
                binary_operation.operator == '<' and 
                is_zero(binary_operation.left_expression)
            )

        results = []

        for source_unit in self.source_units:
            binary_operations = source_unit.get_instances_of(BinaryOperation)
            binary_operations = filter(is_more_than_zero_comparison, binary_operations)
            results.extend(binary_operations)

        return self.generate_results_from_core_objects(results)