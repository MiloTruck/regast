from typing import Dict, List, Tuple
from regast.analysis.core_memoization import memoize_core_objects

from regast.analysis.name_resolution import NameResolver
from regast.core.declarations.source_unit import SourceUnit
from regast.detectors.detector import Detector
from regast.detectors.result import Result
from regast.parsing.parser import Parser


class Regast:
    def __init__(
        self, 
        fnames: List[str], 
        files_in_scope: List[str],
    ):
        self.fnames: List[str] = fnames
        self.files_in_scope: List[str] = files_in_scope
        self.fname_to_source_unit: Dict[str, SourceUnit] = {}

        self._detectors: List[Detector] = []

        # Parse all files with tree-sitter
        self.parser = Parser()
        for fname in self.fnames:
            source_unit = self.parser.parse(fname)
            memoize_core_objects(source_unit)
            self.fname_to_source_unit[fname] = source_unit

        # Name resolution
        # name_resolver = NameResolver()
        # for source_unit in self.fname_to_source_unit.values():
        #     name_resolver.add_source_unit(source_unit)
        # name_resolver.resolve_names()
        
    def register_detector(self, detector_class: Detector):
        instance = detector_class(self.fname_to_source_unit)
        self._detectors.append(instance)

    def run_detectors(self) -> List[Tuple[Detector, Result]]:
        return [(detector, results) for detector in self._detectors if (results := detector.detect())]        
