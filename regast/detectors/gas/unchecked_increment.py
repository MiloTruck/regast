from typing import List

from regast.core.expressions.update_operation import UpdateOperation
from regast.core.statements.for_statement import ForStatement
from regast.detectors.detector import Detector, DetectorClassification
from regast.detectors.result import Result


class UncheckedIncrement(Detector):
    NAME = 'Increments can be declared `unchecked` in for-loops' 
    CLASSIFICATION = DetectorClassification.GAS
    DESCRIPTION = "From Solidity v0.8 onwards, all arithmetic operations have implicit overflow and underflow checks. As it is impossible for the index to overflow in for-loops, index increments/decrements can be left unchecked to save **[30-40 gas](https://gist.github.com/hrkrshnn/ee8fabd532058307229d65dcd5836ddc#the-increment-in-for-loop-post-condition-can-be-made-unchecked)** per loop iteration."

    def detect(self) -> List[Result]:
        results = []

        for source_unit in self.source_units:
            for_statements = source_unit.get_instances_of(ForStatement)

            # Filter for-loops that have either i++ or i--
            for for_statement in for_statements:
                if isinstance(for_statement.iteration, UpdateOperation):
                    result = self.generate_result_from_core_object(for_statement.iteration)
                    results.append(result)

        return results