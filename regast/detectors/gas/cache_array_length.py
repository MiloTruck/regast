from typing import List

from regast.core.expressions.member_access import MemberAccess
from regast.core.statements.for_statement import ForStatement
from regast.detectors.detector import Detector, DetectorClassification
from regast.detectors.result import Result


class CacheArrayLength(Detector):
    NAME = 'Cache array length outside of for-loops' 
    CLASSIFICATION = DetectorClassification.GAS
    DESCRIPTION = "If not cached, the solidity compiler will always read the length of the array during each iteration. That is, if it is a storage array, this is an extra sload operation (100 additional extra gas for each iteration except for the first) and if it is a memory array, this is an extra mload operation (3 additional gas for each iteration except for the first)."

    def detect(self) -> List[Result]:
        """
        This detector's accuracy can be improved by checking if the type of 
        MemberAccess.object is array alongside the .length check
        """

        # Checks member access for .length
        def has_length_access(obj):
            member_accesses = obj.get_instances_of(MemberAccess)

            for member_access in member_accesses:
                if str(member_access.member) == 'length':
                    return True
            
            return False

        results = []

        for source_unit in self.source_units:
            for_statements = source_unit.get_instances_of(ForStatement)

            for for_statement in for_statements:
                # Check for .length access in for-loop header
                for part in [for_statement.condition, for_statement.iteration]:
                    if has_length_access(part):
                        result = self.generate_result_from_core_object(part)
                        results.append(result)

        return results