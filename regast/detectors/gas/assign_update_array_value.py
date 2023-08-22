from typing import List

from regast.core.expressions.array_access import ArrayAccess
from regast.core.expressions.assignment_operation import AssignmentOperation
from regast.core.expressions.binary_operation import BinaryOperation
from regast.detectors.detector import Detector, DetectorClassification
from regast.detectors.result import Result


class AssignUpdateArrayValue(Detector):
    NAME = 'Update array values using `arr[i] += n` instead of `arr[i] = arr[i] + n`' 
    CLASSIFICATION = DetectorClassification.GAS
    DESCRIPTION = "When updating a value in an array with arithmetic, using `array[index] += amount` is cheaper than `array[index] = array[index] + amount`.\nThis is because you avoid an additonal `mload` when the array is stored in memory, and an `sload` when the array is stored in storage.\nThis can be applied for any arithmetic operation including `+=`, `-=`,`/=`,`*=`,`^=`,`&=`, `%=`, `<<=`,`>>=`, and `>>>=`.\nThis optimization can be particularly significant if the pattern occurs during a loop.\n\n*Saves 28 gas for a storage array, 38 for a memory array*"

    def detect(self) -> List[Result]:
        # Checks for arr[i] = arr[i] + n pattern
        def is_array_update_assignment(assignment_operation):
            return (
                # Assignment operation has "=" operator
                str(assignment_operation.operator) == '=' and

                # Assigned value is array access - arr[x] = ...
                isinstance(assignment_operation.left_expression, ArrayAccess) and

                # Right expression is a binary operation - ... = <x> + <y>
                isinstance(binary_operation := assignment_operation.right_expression, BinaryOperation) and

                # Binary Operation has one of the following operators
                str(binary_operation.operator) in ["*", "/", "%", "+", "-", "<<", ">>", ">>>", "&", "^", "|"] and

                # Checks for <x> = <x> + ... or <x> = ... + <x>
                assignment_operation.left_expression in [binary_operation.left_expression, binary_operation.right_expression]
            )

        results = []

        for source_unit in self.source_units:
            assignment_operations = source_unit.get_instances_of(AssignmentOperation)
            assignment_operations = filter(is_array_update_assignment, assignment_operations)
            results.extend(assignment_operations)

        return self.generate_results_from_core_objects(results)