from typing import List

from regast.core.common import Visibility
from regast.core.variables.state_variable import StateVariableMutability
from regast.detectors.detector import Detector, DetectorClassification
from regast.detectors.result import Result


class PrivateConstant(Detector):
    NAME = 'Declare constants as `private` instead of non-public to save gas' 
    CLASSIFICATION = DetectorClassification.GAS
    DESCRIPTION = "If needed, the values can be read from the verified contract source code, or if there are multiple values there can be a single getter function that [returns a tuple](https://github.com/code-423n4/2022-08-frax/blob/90f55a9ce4e25bceed3a74290b854341d8de6afa/src/contracts/FraxlendPair.sol#L156-L178) of the values of all currently-public constants. Saves **3406-3606 gas** in deployment gas due to the compiler not having to create non-payable getter functions for deployment calldata, not having to store the bytes of the value outside of where it's used, and not adding another entry to the method ID table"

    def detect(self) -> List[Result]:
        # Checks for non-private state variables that are constants
        def is_non_private_constant(state_variable):
            return (
                state_variable.mutability == StateVariableMutability.CONSTANT and
                state_variable.visibility != Visibility.PRIVATE
            )
        
        results = []

        for source_unit in self.source_units:
            for contract in source_unit.all_contracts:
                non_constant_state_variables = filter(
                    is_non_private_constant, 
                    contract.state_variables
                )
                results.extend(non_constant_state_variables)

        return self.generate_results_from_core_objects(results)