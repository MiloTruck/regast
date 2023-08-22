from typing import List

from regast.core.expressions.binary_operation import BinaryOperation
from regast.core.expressions.call_expression import CallExpression
from regast.core.expressions.literal import Literal, LiteralType
from regast.detectors.detector import Detector, DetectorClassification
from regast.detectors.result import Result


class SplitRequireStatements(Detector):
    NAME = 'Use separate `require` statements instead of `&&`' 
    CLASSIFICATION = DetectorClassification.GAS

    def detect(self) -> List[Result]:
        # Check if call expression is a require statement, taken from CustomError
        # https://github.com/MiloTruck/regast/blob/main/regast/detectors/gas/custom_error.py
        def is_require_statement(call_expression):
            return (
                str(call_expression.function_name) == 'require' and
                len(call_expression.arguments) == 2 and
                not call_expression.struct_arguments and
                isinstance(error_message := call_expression.arguments[1], Literal) and
                error_message.type == LiteralType.STRING
            )

        # Checks for require statements with &&
        def is_chained_require_statement(call_expression):
            return (
                is_require_statement(call_expression) and 
                isinstance(condition := call_expression.arguments[0], BinaryOperation) and
                str(condition.operator) == '&&'
            )

        results = []

        for source_unit in self.source_units:
            call_expressions = source_unit.get_instances_of(CallExpression)
            call_expressions = filter(is_chained_require_statement, call_expressions)
            results.extend(call_expressions)

        return self.generate_results_from_core_objects(results)