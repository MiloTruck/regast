from typing import List

from regast.core.types.elementary_type import ElementaryType
from regast.core.variables.state_variable import StateVariable, StateVariableMutability
from regast.detectors.detector import Detector, DetectorClassification
from regast.detectors.result import Result


class ByteConstant(Detector):
    NAME = '`bytes` constants are more efficient than `string` constants' 
    CLASSIFICATION = DetectorClassification.GAS

    def detect(self) -> List[Result]:
        # Check if state variable is a string constant
        def is_string_constant(state_variable):
            return (
                state_variable.mutability == StateVariableMutability.CONSTANT and
                isinstance(elementary_type := state_variable.type, ElementaryType) and
                elementary_type.type == 'string'
            )

        results = []

        for source_unit in self.source_units:
            for contract in source_unit.contracts:
                state_variables = contract.get_instances_of(StateVariable)
                string_constants = filter(is_string_constant, state_variables)
                results.extend(string_constants)

        return self.generate_results_from_core_objects(results)