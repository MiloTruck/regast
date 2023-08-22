from typing import List

from regast.core.expressions.binary_operation import BinaryOperation
from regast.core.expressions.call_expression import CallExpression
from regast.detectors.detector import Detector, DetectorClassification
from regast.detectors.result import Result

"""
Find require statements which check that an unsigned integer is more than 0. For example:

```Solidity
require(a > 0, "error");
require(0 < b, "error");
"""

# All detectors inherit from the Detector class
class ExampleASTDetector(Detector):
    # Detector's name
    NAME: str = 'Example Detector'

    # Detector's classification, can be one of the following: GAS, QA, LOW, MEDIUM, HIGH
    CLASSIFICATION: DetectorClassification = DetectorClassification.GAS

    # `detect` function which results a list of Results
    def detect(self) -> List[Result]:
        # List which contains Results
        results = []

        # Iterate through all instances of SourceUnit
        for source_unit in self.source_units:
            # Find all instances of CallExpression in each source unit
            call_expressions = source_unit.get_instances_of(CallExpression)

            # Iterate through all instances of CallExpression
            for call_expression in call_expressions:
                # Filter CallExpression to find "require" calls:
                # 1. function_name must be "require"
                # 2. Must have 2 arguments
                # 3. Must not have any struct arguments
                if (
                    str(call_expression.function_name) == 'require' and
                    len(call_expression.arguments) == 2 and
                    not call_expression.struct_arguments
                ):
                    # Get the first argument of "require" call
                    criteria = call_expression.arguments[0]

                    # Check that criteria is either "a > 0" or "0 < a":
                    # 1. criteria must be an instance of BinaryOperation
                    # 2. right_expression is 0 and operator is ">"
                    # 3. OR the inverse - left_expression is 0 and operator is "<"
                    if (
                        isinstance(criteria, BinaryOperation) and
                        (str(criteria.right_expression) == '0' and str(criteria.operator) == '>' or
                        str(criteria.left_expression) == '0' and str(criteria.operator) == '<')
                    ):  
                        # Generate a Result from the CallExpression object
                        result = self.generate_result_from_core_object(call_expression)

                        # Append result to list of results
                        results.append(result)

        # Return the list of Results
        return results