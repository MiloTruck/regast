from typing import List

from regast.core.expressions.binary_operation import BinaryOperation
from regast.core.expressions.literal import Literal, LiteralType
from regast.detectors.detector import Detector, DetectorClassification
from regast.detectors.result import Result


class ShiftArithmetic(Detector):
    NAME = 'Use `<<` and `>>` instead of multiplication/division where possible' 
    CLASSIFICATION = DetectorClassification.GAS
    DESCRIPTION = "A division/multiplication by any number `x` being a power of 2 can be calculated by shifting `log2(x)` to the right/left.\n\nWhile the `MUL` and `DIV` opcodes use 5 gas, the `SHL` and `SHR` opcodes only uses 3 gas. Furthermore, Solidity's division operation also includes a division-by-0 prevention which is bypassed using shifting."

    def detect(self) -> List[Result]:
        # Checks if n is a power of two (ie. 2**x = n)
        def is_power_two(n):
            return (n & (n-1) == 0) and n != 0

        # Checks if an expression is a number with power two
        def is_literal_power_two(expression):
            return (
                isinstance(expression, Literal) and
                expression.type in [LiteralType.NUMBER, LiteralType.HEX_STRING] and
                is_power_two(expression.value)
            )
        
        # Checks for binary operations that can be replaced with shift arithmetic
        def is_shiftable_binary_operation(binary_operation):
            return (
                is_literal_power_two(binary_operation.left_expression) and
                str(binary_operation.operator) == '*' or
                is_literal_power_two(binary_operation.right_expression) and
                str(binary_operation.operator) in ['*', '/']
            )
        
        results = []

        for source_unit in self.source_units:
            binary_operations = source_unit.get_instances_of(BinaryOperation)
            binary_operations = filter(is_shiftable_binary_operation, binary_operations)
            results.extend(binary_operations)

        return self.generate_results_from_core_objects(results)