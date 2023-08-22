import re
from enum import Enum
from typing import Dict, List
from abc import ABC, abstractmethod

from regast.core.core import Core
from regast.core.declarations.contracts.contract import Contract
from regast.core.declarations.source_unit import SourceUnit
from regast.detectors.result import Result


class DetectorClassification(str, Enum):
    GAS = 'G'
    NC = 'N'
    LOW = 'L'
    MEDIUM = 'M'
    HIGH = 'H'

    def __str__(self):
        return self.value

class Detector(ABC):
    def __init__(self, fname_to_source_unit: Dict[str, SourceUnit]):
        self._fname_to_source_unit: Dict[str, SourceUnit] = fname_to_source_unit
        self._contracts: List[Contract] = []

    @property
    def fnames(self) -> List[str]:
        return list(self._fname_to_source_unit.keys())
    
    @property
    def source_units(self) -> List[SourceUnit]:
        return list(self._fname_to_source_unit.values())

    @property
    def all_contracts(self) -> List[Contract]:
        if not self._contracts:
            self._contracts = [c for su in self.source_units for c in su.all_contracts]
        return list(self.contracts)
    
    @property
    def results(self) -> List[Result]:
        return list(self._results)
    
    def generate_result_from_core_object(self, obj: Core) -> Result:
        source_unit = self._fname_to_source_unit[obj.ast_node.fname]
        source = source_unit.ast_node.text
        return Result.from_node(source, obj.ast_node)
    
    def generate_results_from_core_objects(self, objs: List[Core]) -> List[Result]:
        return [self.generate_result_from_core_object(o) for o in objs]

    def add_results_with_regex(self, regex_pattern: str) -> List[Result]:
        results = []
        
        for fname, source_unit in self._fname_to_source_unit.items():
            source = source_unit.ast_node.text
            lines = source.splitlines()
            
            for line_number, line in enumerate(lines):
                if re.search(regex_pattern, line):
                    result = Result.from_line(
                        fname,
                        source,
                        line_number + 1,
                        line_number + 1
                    )
                    results.append(result)

        return results
    
    @property
    @abstractmethod
    def NAME(self) -> str:
        pass

    @property
    @abstractmethod
    def CLASSIFICATION(self) -> DetectorClassification:
        pass

    @property
    def DESCRIPTION(self) -> str:
        return ''

    @abstractmethod
    def detect(self) -> List[Result]:
        pass