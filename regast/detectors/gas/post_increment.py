from typing import List

from regast.core.expressions.assignment_operation import AssignmentOperation
from regast.core.expressions.literal import Literal, LiteralType
from regast.core.expressions.update_operation import UpdateOperation
from regast.detectors.detector import Detector, DetectorClassification
from regast.detectors.result import Result


class PostIncrement(Detector):
    NAME = '`++i` costs less gas than `i++` or `i += 1`' 
    CLASSIFICATION = DetectorClassification.GAS
    DESCRIPTION = "Pre-increments and pre-decrements are cheaper than post-increments and post-decrements"

    def detect(self) -> List[Result]:
        # Checks for i += 1 or i -= 1
        def is_plus_equal_one(assignment_operation):
            return (
                str(assignment_operation.operator) in ['+=', '-='] and
                isinstance(literal := assignment_operation.right_expression, Literal) and
                literal.type in [LiteralType.NUMBER, LiteralType.HEX_STRING] and
                literal.value == 0
            )
        
        results = []

        for source_unit in self.source_units:
            # Find all instances of i++ or i--
            update_operations = source_unit.get_instances_of(UpdateOperation)
            update_operations = [uo for uo in update_operations if not uo.is_prefix]

            # Find all instances of i += 1 or i -= 1
            assignment_operations = source_unit.get_instances_of(AssignmentOperation)
            assignment_operations = filter(is_plus_equal_one, assignment_operations)

            results.extend(update_operations + list(assignment_operations))

        return self.generate_results_from_core_objects(results)