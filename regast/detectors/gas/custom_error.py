from typing import List

from regast.core.expressions.call_expression import CallExpression
from regast.core.expressions.literal import Literal, LiteralType
from regast.detectors.detector import Detector, DetectorClassification
from regast.detectors.result import Result


class CustomError(Detector):
    NAME = 'Use custom errors instead of `require` statements' 
    CLASSIFICATION = DetectorClassification.GAS
    DESCRIPTION = "[Source](https://blog.soliditylang.org/2021/04/21/custom-errors/)\nInstead of using error strings, to reduce deployment and runtime cost, you should use Custom Errors. This would save both deployment and runtime cost."

    def detect(self) -> List[Result]:
        # Check if call expression is a require statement
        def is_require_statement(call_expression):
            return (
                str(call_expression.function_name) == 'require' and
                len(call_expression.arguments) == 2 and
                not call_expression.struct_arguments and
                isinstance(error_message := call_expression.arguments[1], Literal) and
                error_message.type == LiteralType.STRING
            )

        results = []

        for source_unit in self.source_units:
            call_expressions = source_unit.get_instances_of(CallExpression)
            call_expressions = filter(is_require_statement, call_expressions)
            results.extend(call_expressions)
            
        return self.generate_results_from_core_objects(results)