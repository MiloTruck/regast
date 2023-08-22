from typing import List

from regast.detectors.detector import Detector, DetectorClassification
from regast.detectors.result import Result

class YourDetectorClass(Detector):
    NAME = ''
    CLASSIFICATION = DetectorClassification.GAS

    def detect(self) -> List[Result]:
        results = []
        
        return results